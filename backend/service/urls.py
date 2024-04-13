from django.urls import path

from .views import *
from .feeds import *


urlpatterns = [
    path('', home, name='HOME'),
    path('category/<str:slug>/', eachCategory, name='CATEGORY'),
    path('services/', allService, name='SERVICES'),
    path('service/<str:slug>/', eachService, name='SERVICE'),
    path('category-feeds/', CategoryFeed(), name='CATEGORY-FEED'),
    path('service-feeds/', AllServiceFeed(), name='SERVICE-FEED'),
    path('gallery-feeds/', GalleryFeed(), name='GALLERY-FEED'),
]
