from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def emp_data_view(request):
    emp_data = {
    'eno':100,
    'ename':'lipun',
    'esal':10000,
    'eaddr':'Hydrabad',
    }
    return HttpResponse('<h1> Employee Number:{}<br> Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}<br> </h1>'
     .format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'],))

import json
def emp_data_json_view(request):
    emp_data = {
    'eno':100,
    'ename':'lipun',
    'esal':10000,
    'eaddr':'Hydrabad',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')

from django.http import JsonResponse
def emp_data_json_view2(request):
    emp_data = {
    'eno':100,
    'ename':'lipun',
    'esal':10000,
    'eaddr':'Hydrabad',
    }
    return JsonResponse(emp_data)
