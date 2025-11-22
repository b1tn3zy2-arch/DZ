from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['tab_number', 'full_name', 'email', 'phone', 'position']
    search_fields = ['full_name', 'tab_number', 'email']
    list_filter = ['position']