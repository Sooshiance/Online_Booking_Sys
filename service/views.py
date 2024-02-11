from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound

from .models import Category, AllService, Letter
from .forms import Paper


def home(request):
    cat = Category.objects.all()
    serv = AllService.objects.all()
    if request.method == 'POST':
        form = Paper(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            person = Letter.objects.create(email=email)
            person.save()
            messages.success(request, 'با سپاس از مشارکت شما')
            return redirect('HOME')
        else:
            messages.error(request, 'اشتباهی رخ داده، دوباره امتحان کنید')
            return redirect('HOME')
    else:
        form = Paper()
    return render(request, "index.html", {'category':cat, 'services': serv, 'form':form})


def eachCategory(request, slug):
    try:
        cat = Category.objects.get(slug=slug)
        serv = AllService.objects.filter(category__slug=slug)
        return render(request, "each_category.html", {'category':cat, 'services':serv})
    except:
        return HttpResponseNotFound(content="صفحه مورد نظر یافت نشد")


def allService(request):
    try :
        serv = AllService.objects.all()
        return render(request, "allservice.html", {'services': serv})
    except:
        return HttpResponseNotFound(content="صفحه مورد نظر یافت نشد")


def eachService(request, slug):
    try : 
        serv = AllService.objects.get(slug=slug)
        return render(request, "service.html", {'service':serv})
    except:
        return HttpResponseNotFound(content="صفحه مورد نظر یافت نشد")
