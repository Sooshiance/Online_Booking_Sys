import pyotp

from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponseNotAllowed
from django.utils.timezone import datetime

from .models import User, Profile
from .forms import RegisterUser, OTPForm
from .utils import passwordResetEmail
from .otp import sendToken

from arrot.models import ArrotModel, GolsaModel, Wallet
from question.models import Question


########################## Authentication Section ##########################


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, phone=phone, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'خوش آمدید')
            return redirect('HOME')
        else:
            messages.error(request, 'مشخصات وارد شده اشتباه می باشد، دوباره تلاش کنید')
            return render(request, 'login.html')
    return render(request, "login.html")


def logoutUser(request):
    auth.logout(request)
    messages.info(request, 'به امید دیداری دوباره')
    return redirect('HOME')


########################## Register User Section ##########################


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(email=email, password=password,first_name=first_name,
                                            last_name=last_name, phone=phone)
            user.set_password(password)
            user.is_active = False
            user.save()
            request.session["pk"] = user.pk
            sendToken(request=request)
            messages.success(request, 'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('HOME')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('REGISTER')
    else:
        form = RegisterUser()
    return render(request, "signup.html", {'form': form})


def otpRegisterValidation(request):
    form = OTPForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            otp = form.cleaned_data.get("otp")
            pk = request.session["pk"]
            otp_secret_key = request.session["otp_secret_key"]
            otp_valid_until = request.session["otp_valid_date"]
            
            if otp_secret_key and otp_valid_until:
                valid_until = datetime.fromisoformat(otp_valid_until)
                
                if valid_until > datetime.now():
                    totp = pyotp.TOTP(otp_secret_key, interval=180)
                    
                    if totp.verify(otp):
                        print(pk)
                        user = User.objects.get(pk=pk)
                        
                        user.is_active = True
                        
                        user.save()

                        del request.session["otp_secret_key"]
                        del request.session["otp_valid_date"]
                        
                        messages.success(request, '')
                        
                        return redirect('HOME')
                    
                    else:
                        messages.error(request, 'otp is used before or expired')
                        return redirect('OTP-REGISTER-VERIFY')
                else:
                    messages.error(request, 'otp time has passed')
                    return redirect('OTP-REGISTER-VERIFY')
            else:
                messages.error(request, 'the OTP is not acceptable')
                return redirect('REGISTER')
            
        else:
            messages.error(request, '')
            return redirect('REGISTER')
    return render(request, 'otp_register.html', {'form':form})


########################## Profile Page Section ##########################


def userProfile(request):
    if request.user.is_authenticated:
        user = request.user 
        prof = Profile.objects.get(user=request.user)
        arrot_reserved = ArrotModel.objects.filter(user__exact=request.user)
        golsa_reserved = GolsaModel.objects.filter(user__exact=request.user)
        asked = Question.objects.all().filter(user__exact=request.user)
        wallet = Wallet.objects.get(user=user) or None 
        context = {'profile':prof,
                   'arrot':arrot_reserved,
                   'golsa':golsa_reserved,
                   'questions':asked,
                   'wallet':wallet,}
        return render(request, 'profile.html', context=context)
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


def deleteArrotItem(request, pk):
    if request.user.is_authenticated:
        t = ArrotModel.objects.get(pk=pk)
        t.delete()
        user = t.user         
        w = Wallet.objects.get(user=user)
        w.remove_turn()
        print(w.reach_limit)        
        messages.success(request, 'نوبت انتخابی شما، با موفقیت حذف شد')
        return redirect('PROFILE')
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


def deleteGolsaItem(request, pk):
    if request.user.is_authenticated:
        g = GolsaModel.objects.get(pk=pk)
        g.delete()
        user = g.user         
        w = Wallet.objects.get(user=user)
        w.remove_turn()
        print(w.reach_limit)  
        messages.success(request, 'نوبت انتخابی شما، با موفقیت حذف شد')
        return redirect('PROFILE')
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


########################## Password Reset via Email Section ##########################


def forgetPassword(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            passwordResetEmail(request, user)
            messages.success(request, 'لینک بازیابی گذر واژه با موفقیت فرستاده شد')
            return redirect('LOGIN')
        else:
            messages.error(request, 'پست الکترونیکی داده شده اشتباه می باشد')
            return redirect('FORGET')
    return render(request, 'forget_password.html')


def resetLink(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except:
        pass
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'گذر واژه خود را بازیابی کنید')
        return redirect('CONFIRM')
    else:
        messages.error(request, 'توکن نا معتبر است، یا پیش از این استفاده شده')
        return redirect('LOGIN')


def confirmResetting(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'گذر واژه با موفقیت بازیابی شد')
            return redirect('LOGIN')
        else:
            messages.error(request, 'گذر واژه های داده شده همخوانی ندارند، دوباره تلاش کنید')
            return redirect('CONFIRM')
    return render(request, 'confirm_password.html')


########################## Password Reset via OTP Section ##########################


def otpResetPassword(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        if User.objects.filter(phone__exact=phone):
            user = User.objects.get(phone=phone)
            request.session["pk"] = user.pk
            sendToken(request=request)
            messages.success(request, "")
            return redirect('RESET')
        else:
            messages.error(request, "")
            return redirect("FORGET")
    return render(request, "forgetPassowrd.html")


def checkOTP(request):
    form = OTPForm(request.POST, None)
    if request.method == 'POST':
        if form.is_valid():
            otp = form.cleaned_data.get("otp")
            otp_secret_key = request.session["otp_secret_key"]
            otp_valid_until = request.session["otp_valid_date"]
            
            if otp_secret_key and otp_valid_until:
                valid_until = datetime.fromisoformat(otp_valid_until)
                
                if valid_until > datetime.now():
                    totp = pyotp.TOTP(otp_secret_key, interval=180)
                    
                    if totp.verify(otp):
                        messages.success(request, "")

                        del request.session["otp_secret_key"]
                        del request.session["otp_valid_date"]
                        
                        return redirect("CONFIRM")
                    else:
                        messages.error(request, 'otp is used before or expired')
                        return redirect('RESET')
                else:
                    messages.error(request, 'otp time has passed')
                    return redirect('FORGET')
            else:
                messages.error(request, 'the OTP is not acceptable')
                return redirect('FORGET')
        else:
            messages.error(request, "")
            return redirect("FORGET")
    return render(request, "otp_reset_password.html", {"form":form})


def confirmResetPassowrd(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password == confirm_password:
            pk = request.session.get("pk")
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'گذر واژه با موفقیت بازیابی شد')
            return redirect('LOGIN')
        else:
            messages.error(request, "")
            return redirect("CONFIRM")
    return render(request, "confirm_password.html")


########################## Admin panel ##########################


def adminPrivileges(request):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            w = Wallet.objects.all().filter(reach_limit=20)
            return render(request, 'admin_panel.html', {"users_reach_limit":w})
        else:
            return HttpResponseNotAllowed("you are not superuser!")
    else:
        return redirect('LOGIN')
