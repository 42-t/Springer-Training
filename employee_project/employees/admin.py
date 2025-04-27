from django.contrib import admin


from .models import Employee, Department, Performance

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Performance)

