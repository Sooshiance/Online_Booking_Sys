from django.urls import path

from .views import *


urlpatterns = [
    path('', loginUser, name='LOGIN'),
    path('logout/', logoutUser, name='LOGOUT'),
    path('register/', registerUser, name='REGISTER'),
    path('profile/', userProfile, name='PROFILE'),
    path('delete-arrot/<int:pk>/', deleteArrotItem, name='DELETEARROT'),
    path('delete-golsa/<int:pk>/', deleteGolsaItem, name='DELETEGOLSA'),
    path('forgetpassword/', forgetPassword, name='FORGET'),
    path('reset/<uidb64>/<token>/', resetLink, name='RESET'),
    path('confirm/', confirmResetting, name='CONFIRM'),
]
