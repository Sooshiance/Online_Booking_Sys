from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import HttpResponseNotFound

from .models import Category, AllService, Letter
from .forms import Paper


def home(request):
    connection.force_debug_cursor = True
    cat = Category.objects.all()
    serv = AllService.objects.all()
    av_serv = AllService.objects.all().filter(is_available=True)
    connection.force_debug_cursor = False
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
    return render(request, "service/index.html", {'category':cat,'services':serv,'form':form,'available':av_serv})


def eachCategory(request, slug):
    try:
        connection.force_debug_cursor = True
        cat = Category.objects.get(slug=slug)
        serv = AllService.objects.filter(category__slug=slug)
        connection.force_debug_cursor = False
        return render(request, "service/each_category.html", {'category':cat, 'services':serv})
    except:
        return HttpResponseNotFound(content="صفحه مورد نظر یافت نشد")


def allService(request):
    try :
        connection.force_debug_cursor = True
        serv = AllService.objects.all()
        av_serv = AllService.objects.all().filter(is_available=True)
        connection.force_debug_cursor = False
        return render(request, "service/allservice.html", {'services': serv, 'available':av_serv})
    except:
        return HttpResponseNotFound(content="صفحه مورد نظر یافت نشد")


def eachService(request, slug):
    try : 
        connection.force_debug_cursor = True
        serv = AllService.objects.get(slug=slug)
        connection.force_debug_cursor = False
        return render(request, "service/service.html", {'service':serv})
    except:
        return HttpResponseNotFound(content="صفحه مورد نظر یافت نشد")
