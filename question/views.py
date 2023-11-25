from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import Ask
from .models import RepetitiveQuestion, Question


def dailyQuestion(request):
    rq = RepetitiveQuestion.objects.all().order_by('created_at')
    return render(request, "daily.html", {'questions': rq})


def askQuestion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Ask(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                txt = form.cleaned_data['txt']
                q = Question.objects.create(title=title, txt=txt, user=request.user)
                q.save()
                messages.success(request, 'پرسش شما با موفقیت ثبت شد،پاسخ به پست الکترونیکی شما ارسال خواهد شد')
                return redirect('DAILY')
            else:
                messages.error(request, 'اشتباهی رخ داده است، دوباره تلاش کنید')
                return redirect('ASKS')
        else:
            form = Ask()
        return render(request, 'ask.html', {'form':form})
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')
