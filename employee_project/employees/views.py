from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from datetime import datetime

from .models import Department, Employee, Attendance, Performance
from .serializers import *

# ----- ViewSets -----
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['department', 'date_joined']
    ordering_fields = ['name', 'date_joined']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

# ----- Custom API Views -----
@api_view(['GET'])
def department_employee_count(request):
    data = Employee.objects.values('department').annotate(count=Count('id'))
    return Response(data)

@api_view(['GET'])
def monthly_attendance_overview(request):
    this_year = datetime.now().year
    data = Attendance.objects.filter(date__year=this_year) \
        .values('date__month') \
        .annotate(count=Count('id')) \
        .order_by('date__month')
    return Response(data)

# ----- Frontend Template View -----
def dashboard(request):
    return render(request, 'dashboard.html')
