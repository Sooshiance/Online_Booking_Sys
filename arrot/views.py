from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ArrotModel, GolsaModel
from .forms import ClinicReserve, SalonReserve


def reserveLink(request):
    return render(request, "reservation.html")


def reserveClinicView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ClinicReserve(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                date = form.cleaned_data['date']
                hour = form.cleaned_data['hour']
                description = form.cleaned_data['description']
                object = ArrotModel.objects.create(title=title, date=date, hour=hour, description=description,
                                                    user=request.user)
                object.save()
                messages.success(request, 'نوبت شما با موفقیت ذخیره شد')
                return redirect('RESERVED')
            else:
                messages.error(request, f'{form.errors}')
                form = ClinicReserve()
                return render(request, 'clinic.html', {'form': form})
        else:
            form = ClinicReserve()
        return render(request, 'clinic.html', {'form':form})
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


def reserveSalonView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SalonReserve(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                date = form.cleaned_data['date']
                hour = form.cleaned_data['hour']
                description = form.cleaned_data['description']
                object = GolsaModel.objects.create(title=title, date=date, hour=hour, description=description,
                                                    user=request.user)
                object.save()
                messages.success(request, 'نوبت شما با موفقیت ذخیره شد')
                return redirect('RESERVED')
            else:
                messages.error(request, f"{form.errors}")
                form = SalonReserve()
                return render(request, 'salon.html', {'form': form})
        else:
            form = SalonReserve()
            return render(request, 'salon.html', {'form':form})
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')
