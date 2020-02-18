from django.shortcuts import render
from webapp.models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from webapp.mixin import SerializeMixin, HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from webapp.utils import is_json
from webapp.forms import EmployeeForm
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDView(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp
    # Get Operation
    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please Provide Valid Json data'})
            return self.render_to_http_response(json_data)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg':'No Record Available For This ID '})
                return self.render_to_http_response(json_data)
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
    #Create Operation
    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please Provide Valid Json data'})
            return self.render_to_http_response(json_data, status_code=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource Created'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status_code=400)
    #Update Operation
    def put(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please Provide Valid Json Data'})
            return self.render_to_http_response(json_data)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is None:
            json_data = json.dumps({'msg':"To perform Updation ID is Mandatory, please Provide ID"})
            return self.render_to_http_response(json_data)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':"No Record Found With This ID can't perform Update Operation, Please Provide Valid ID"})
            return self.render_to_http_response(json_data)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource Update successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data)
    #Delete Operation
    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please Provide Valid Json data'})
            return self.render_to_http_response(json_data)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg':'No Record Available For This ID '})
                return self.render_to_http_response(json_data)
            t = emp.delete()
            print(t)
            json_data = json.dumps({'msg':'Delete successfully Done'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':"To perform Deletion ID is Mandatory, please Provide ID"})
        return self.render_to_http_response(json_data)














@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailsCBView(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self, request, id, *args,**kwargs):
        try:
            qs = Employee.objects.get(id=id)
        except Exception as messages:
            json_data = json.dumps({'msg':'The requested resource not available'})
        else:
            json_data = serialize('json', [qs,])
        # emp_data={
        # 'eno':emp.eno,
        # 'ename': emp.ename,
        # 'esal': emp.esal,
        # 'eaddr': emp.eaddr,
        # }
        # json_data =json.dumps(emp_data) | fields=('eno','ename','eaddr')

        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No Match Found For This ID'})
            return self.render_to_http_response(json_data)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please Provide Valid Json data'})
            return self.render_to_http_response(json_data)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource Update successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status_code=400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No Match Found For This ID can not do delete operations'})
            return self.render_to_http_response(json_data)
        t = emp.delete()
        print(t)
        json_data = json.dumps({'msg':'Delete successfully Done'})
        return self.render_to_http_response(json_data)


# @method_decorator(csrf_exempt, name='dispatch')
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin, View):
#     def get(self, request, *args,**kwargs):
#         qs = Employee.objects.all()
#         # json_data = serialize('json', qs)
#         # p_data = json.loads(json_data)
#         # final_data=[]
#         # for obj in p_data:
#         #     emp_data = obj['fields']
#         #     final_data.append(emp_data)
#         # json_data = json.dumps(final_data)
#         json_data = self.serialize(qs)
#
#         return HttpResponse(json_data, content_type='application/json')
#
    # def post(self, request, *args, **kwargs):
    #     data = request.body
    #     valid_json = is_json(data)
    #     if not valid_json:
    #         json_data = json.dumps({'msg':'Please Provide Valid Json data'})
    #         return self.render_to_http_response(json_data, status_code=400)
    #     empdata = json.loads(data)
    #     form = EmployeeForm(empdata)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         json_data = json.dumps({'msg':'Resource Created'})
    #         return self.render_to_http_response(json_data)
    #     if form.errors:
    #         json_data = json.dumps(form.errors)
    #         return self.render_to_http_response(json_data, status_code=400)
