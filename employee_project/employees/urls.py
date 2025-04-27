from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)   # 👈 use views.EmployeeViewSet
router.register(r'departments', views.DepartmentViewSet)
router.register(r'attendance', views.AttendanceViewSet)
router.register(r'performance', views.PerformanceViewSet)

urlpatterns = [
    # APIs from ViewSets
    path('', include(router.urls)),

    # Custom APIs
    path('department-count/', views.department_employee_count, name='department-count'),
    path('monthly-attendance/', views.monthly_attendance_overview, name='monthly-attendance'),

    # Dashboard Page
    path('dashboard/', views.dashboard, name='dashboard'),
]
