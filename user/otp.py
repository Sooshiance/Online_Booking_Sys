import pyotp 
from decouple import config

from django.utils.timezone import datetime, timedelta

from sms_ir import SmsIr


def sendToken(request, phone):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=180)
    
    otp = totp.now()
    
    request.session["otp_secret_key"] = totp.secret
    
    valid_date = datetime.now() + timedelta(minutes=3)
    
    request.session["otp_valid_date"] = str(valid_date)
    
    print(f"The OTP is : {otp}")
    
    user_sms = SmsIr(api_key=config("API_KEY", cast=str), linenumber=config("MY_NUMBER", cast=str))
    
    user_sms.send_sms(number=phone, message="""
                      کد احراز هویت شما در سامانه آروت
                      """, linenumber=config("MY_NUMBER", cast=str))
    
    # send a SMS to User's verified Phone number
