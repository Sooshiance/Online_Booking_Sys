from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='HOME'),
    path('category/<str:slug>/', eachCategory, name='CATEGORY'),
    path('services/', allService, name='SERVICES'),
    path('service/<str:slug>/', eachService, name='SERVICE'),
]
