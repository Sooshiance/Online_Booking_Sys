from django.urls import path

from .views import *


urlpatterns = [
    path('', showComment, name='SHOW'),
    path('share/', shareComment, name='SHARE'),
]
