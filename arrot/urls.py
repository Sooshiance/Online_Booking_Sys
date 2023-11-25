from django.urls import path

from .views import *


urlpatterns = [
    path('', reserveLink, name='RESERVED'),
    path('clinic/', reserveClinicView, name='CLINIC'),
    path('salon/', reserveSalonView, name='SALON'),
]
