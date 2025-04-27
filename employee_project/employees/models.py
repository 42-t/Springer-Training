from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date_joined = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
class Performance(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating}"