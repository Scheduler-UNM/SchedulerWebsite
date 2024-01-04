from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="employee"),
    path('<int:employee_id>/', views.employee_details, name='employee_details'),
    #path("add-shifts/", views.add_shifts_to_employee_view, name="add"),
]