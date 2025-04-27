from django.core.management.base import BaseCommand
from employees.models import Employee, Department, Attendance, Performance
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()




class Command(BaseCommand):
    help = 'Seed the database with fake employees, departments, attendance, and performance'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Deleting old data..."))
        Employee.objects.all().delete()
        Department.objects.all().delete()
        Attendance.objects.all().delete()
        Performance.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Creating departments..."))
        departments = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']
        dept_objs = []
        for name in departments:
            dept = Department.objects.create(name=name)
            dept_objs.append(dept)

        self.stdout.write(self.style.SUCCESS("Creating employees and related records..."))
        for _ in range(50):
            dept = random.choice(dept_objs)
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=dept
            )

            # Create 5 attendance records per employee
            for i in range(5):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['present', 'absent', 'late'])
                )

            # Create performance review
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_this_year()
            )

        self.stdout.write(self.style.SUCCESS("Done seeding fake data!"))
