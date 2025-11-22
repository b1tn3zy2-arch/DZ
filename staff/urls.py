from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('schedule/', views.schedule, name='schedule'),
    path('add/', views.add_employee, name='add_employee'),
]