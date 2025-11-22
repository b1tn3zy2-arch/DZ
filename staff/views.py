from django.shortcuts import render, redirect
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all().order_by('tab_number')

    if not employees.exists():
        Employee.objects.create(
            tab_number="00001",
            full_name="Смирнова Мария Михайловна",
            email="smirnova@gmail.com",
            phone="8(495)344 99 33",
            position="менеджер"
        )
        Employee.objects.create(
            tab_number="00002",
            full_name="Иванов Иван Иванович",
            email="ivanov@company.com",
            phone="8(495)555 44 33",
            position="аналитик"
        )
        Employee.objects.create(
            tab_number="00003",
            full_name="Петрова Анна Сергеевна",
            email="petrova@company.com",
            phone="8(495)666 77 88",
            position="дизайнер"
        )
        employees = Employee.objects.all().order_by('tab_number')

    return render(request, 'staff/employee_list.html', {'employees': employees})


def schedule(request):
    return render(request, 'staff/schedule.html')


def add_employee(request):
    if request.method == 'POST':
        tab_number = request.POST.get('tab_number')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        position = request.POST.get('position')

        if Employee.objects.filter(tab_number=tab_number).exists():
            employee = Employee.objects.get(tab_number=tab_number)
            employee.full_name = full_name
            employee.email = email
            employee.phone = phone
            employee.position = position
            employee.save()
        else:
            # Если не существует, создаем нового
            Employee.objects.create(
                tab_number=tab_number,
                full_name=full_name,
                email=email,
                phone=phone,
                position=position
            )

        return redirect('employee_list')

    return render(request, 'staff/add_employee.html')