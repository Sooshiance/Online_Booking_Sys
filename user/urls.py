from django.urls import path

from .views import *


urlpatterns = [
    # TODO :Authentication
    path('', loginUser, name='LOGIN'),
    path('logout/', logoutUser, name='LOGOUT'),
    path('profile/', userProfile, name='PROFILE'),
    path('profile/update/<int:pk>/', updateProfile, name='UPDATE-PROFILE'),
    
    # TODO : Register
    path('register/', registerUser, name='REGISTER'),
    path('register/otp/', otpRegisterValidation, name='OTP-REGISTER'),
    
    # TODO : Email Reset password
    path('forgetpassword/', forgetPassword, name='FORGET'),
    path('reset/<uidb64>/<token>/', resetLink, name='RESET'),
    path('confirm/', confirmResetting, name='CONFIRM'),
    
    # TODO : OTP reset password
    path('otp/forgetpassword/', otpResetPassword, name='OTP-FORGET'),
    path('otp/check/', checkOTP, name='OTP-RESET'),
    path('otp/reset-link/', confirmResetPassowrd, name='OTP-CONFIRM'),
    
    # TODO : Admin checks the users who reached at maximum mount in their Wallet
    path('users/wallet/', adminPrivileges),
]
