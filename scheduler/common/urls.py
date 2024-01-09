from django.urls import path
from . import views

urlpatterns = [
    path('',views.save_terms,name='save_terms'),
    path('pod', views.create_pod, name='create-pod'),
    path('shift/', views.create_shift, name='create_shift'),
]
