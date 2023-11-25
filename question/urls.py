from django.urls import path

from .views import *


# app_name = 'QUESTIONS'

urlpatterns = [
    path('', dailyQuestion, name='DAILY'),
    path('ask/', askQuestion, name='ASKS'),
]
