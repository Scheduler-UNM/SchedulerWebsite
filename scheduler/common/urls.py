from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.create_pod, name='create-pod'),
    path('shift/', views.create_shift, name='create_shift'),
]
