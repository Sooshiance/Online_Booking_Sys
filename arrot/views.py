from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import ArrotModel, GolsaModel, Wallet
from .forms import *


def reserveLink(request):
    return render(request, "arrot/reservation.html")


############################ TODO : Clinic reservation ############################


def reserveClinicView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClinicReserve(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                date = form.cleaned_data['date']
                jtime = form.cleaned_data['jtime']
                hour = form.cleaned_data['hour']
                description = form.cleaned_data['description']
                
                object = ArrotModel.objects.create(title=title, date=date, hour=hour, description=description,
                                                    user=request.user, jtime=jtime)                
                object.save()
                messages.success(request, 'نوبت شما با موفقیت ذخیره شد')
                return redirect('RESERVED')
            else:
                messages.error(request, f'{form.errors}')
                form = ClinicReserve()
                return render(request, 'arrot/clinic.html', {'form': form})
        else:
            form = ClinicReserve()
        return render(request, 'arrot/clinic.html', {'form':form})
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


def changingArrotItem(request, pk):
    if request.user.is_authenticated:
        form = RepairClinic(request.POST or None)
        obj = get_object_or_404(ArrotModel, pk=pk)
        auth_user = request.user
        if request.method == "POST":
            if form.is_valid() and obj is not None:
                title = form.cleaned_data['title']
                date = form.cleaned_data['date']
                jtime = form.cleaned_data['jtime']
                description = form.cleaned_data['description']
                obj.title = title
                obj.date = date
                obj.jtime = jtime
                obj.description = description
                obj.save()
                messages.success(request, "")
                return redirect('PROFILE')
            else:
                messages.error(request, "")
                return redirect("CHANGEARROT")
        context = {'field':obj, 'user':auth_user, 'form':form}
        return render(request, "arrot/change_arrot.html", context=context)
    else:
        messages.info(request, "")
        return redirect("LOGIN")


def deleteArrotItem(request, pk):
    if request.user.is_authenticated:
        obj = get_object_or_404(ArrotModel, pk=pk)
        auth_user = request.user
        context = {'field':obj, 'user':auth_user}
        if request.method=="POST" and get_object_or_404(ArrotModel, pk=pk):
            obj = ArrotModel.objects.get(pk=pk)
            obj.delete()
            user = obj.user 
            w = Wallet.objects.get(user=user)
            w.remove_turn()
            print(w.reach_limit)        
            messages.success(request, 'نوبت انتخابی شما، با موفقیت حذف شد')
            return redirect('PROFILE')
        return render(request, "arrot/delete_arrot.html", context=context)
        
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


############################ TODO : Salon reservation ############################


def reserveSalonView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SalonReserve(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                date = form.cleaned_data['date']
                jtime = form.cleaned_data['jtime']
                hour = form.cleaned_data['hour']
                description = form.cleaned_data['description']
                
                object = GolsaModel.objects.create(title=title, date=date, hour=hour, description=description,
                                                    user=request.user, jtime=jtime)
                object.save()
                messages.success(request, 'نوبت شما با موفقیت ذخیره شد')
                return redirect('RESERVED')
            else:
                messages.error(request, f"{form.errors}")
                form = SalonReserve()
                return render(request, 'arrot/salon.html', {'form': form})
        else:
            form = SalonReserve()
            return render(request, 'arrot/salon.html', {'form':form})
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


def deleteGolsaItem(request, pk):
    if request.user.is_authenticated:
        obj = get_object_or_404(GolsaModel, pk=pk)
        auth_user = request.user
        context = {'field':obj, 'user':auth_user}
        if request.method == "POST" and obj is not None:
            g = GolsaModel.objects.get(pk=pk)
            g.delete()
            user = g.user         
            w = Wallet.objects.get(user=user)
            w.remove_turn()
            print(w.reach_limit)  
            messages.success(request, 'نوبت انتخابی شما، با موفقیت حذف شد')
            return redirect('PROFILE')
        return render(request, "arrot/delete_golsa.html", context=context)
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


def changingGolsaItem(request, pk):
    if request.user.is_authenticated:
        form = SalonReserve(request.POST or None)
        obj = get_object_or_404(GolsaModel, pk=pk)
        auth_user = request.user
        if request.method == "POST":
            if form.is_valid() and obj is not None:
                title = form.cleaned_data['title']
                date = form.cleaned_data['date']
                jtime = form.cleaned_data['jtime']
                description = form.cleaned_data['description']
                obj.title = title
                obj.date = date
                obj.jtime = jtime
                obj.description = description
                obj.save()
                messages.success(request, "")
                return redirect("PROFILE")
            else:
                messages.error(request, "")
                return redirect("CHANGEGOLSA")
        context = {'field':obj, 'user':auth_user, 'form':form}
        return render(request, "arrot/change_golsa.html", context=context)
    else:
        messages.info(request, "")
        return redirect("LOGIN")
