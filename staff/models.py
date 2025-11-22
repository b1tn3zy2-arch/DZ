from django.db import models

class Employee(models.Model):
    tab_number = models.CharField(max_length=10, unique=True, verbose_name="Табельный номер")
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    position = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"