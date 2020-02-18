from django.shortcuts import render
from webapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from webapp.models import Employee
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class EmployeeViewSetCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
