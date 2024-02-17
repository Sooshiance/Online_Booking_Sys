from django.urls import path

from .views import *


urlpatterns = [
    path('', reserveLink, name='RESERVED'),
    path('clinic/', reserveClinicView, name='CLINIC'),
    path('salon/', reserveSalonView, name='SALON'),

    # TODO : Users control their reserved turns 
    path('profile/delete-arrot/<int:pk>/', deleteArrotItem, name='DELETEARROT'),
    path('profile/delete-golsa/<int:pk>/', deleteGolsaItem, name='DELETEGOLSA'),
    
    # TODO : Users control their reserved turns 
    path('profile/change-arrot/<int:pk>/', changingArrotItem, name='CHANGEARROT'),
    path('profile/change-golsa/<int:pk>/', changingGolsaItem, name='CHANGEGOLSA'),
]
