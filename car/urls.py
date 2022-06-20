from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='car-home'),
    path('about',views.ab, name='car-about'),
]