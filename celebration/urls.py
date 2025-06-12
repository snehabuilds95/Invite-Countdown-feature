from django.urls import path
from . import views

urlpatterns = [
    path('VAIBHAV/', views.coming_soon, name='coming_soon'),
]