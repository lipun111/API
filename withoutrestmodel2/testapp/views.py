from django.shortcuts import render
from django.views.generic import View
from testapp.models import Student
from testapp.utils import is_json
from testapp.mixin import HttpResponseMixin, SerializeMixin
import json
from testapp.forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDView(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            stu = None
        return stu
# Get Operations

    def get(self, request,*args,**kwargs):
        data = request.body
        valid_json= is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Provide some valid json data'})
            return self.render_to_http_response(json_data)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            stu = self.get_object_by_id(id)
            if stu is None:
                json_data = json.dumps({'msg':'Given ID is Not Matched With exsiting record, Please Give some valid ID'})
                return self.render_to_http_response(json_data)
            json_data = self.serialize([stu,])
            return self.render_to_http_response(json_data)
        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)
# Post Operations

    def post(self, request, *args,**kwargs):
        data = request.body
        valid_json= is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Provide some valid json data'})
            return self.render_to_http_response(json_data)
        stu_data = json.loads(data)
        form = StudentForm(stu_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Record created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data)
# Update Operations

    def put(self,request, *args,**kwargs):
        data = request.body
        valid_json= is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Provide some valid json data'})
            return self.render_to_http_response(json_data)
        provided_data = json.loads(data)
        id = provided_data.get('id',None)
        if id is None:
            json_data = json.dumps({'msg':'ID is mandatory for Update Operation, please provide ID'})
            return self.render_to_http_response(json_data)
        stu = self.get_object_by_id(id)
        if stu is None:
            json_data = json.dumps({'msg':'Given ID is Not Matched With exsiting record, Please Give some valid ID'})
            return self.render_to_http_response(json_data)
        original_data ={
        'name':stu.name,
        'rollno':stu.rollno,
        'mark':stu.mark,
        'division':stu.division,
        'addrs':stu.addrs,
        }
        original_data.update(provided_data)
        form = StudentForm(original_data, instance=stu)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Record Updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data)
# Delete Operations

    def delete(self, request, *args,**kwargs):
        data = request.body
        valid_json= is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Provide some valid json data'})
            return self.render_to_http_response(json_data)
        stu_data = json.loads(data)
        id = stu_data.get('id',None)
        if id is None:
            json_data = json.dumps({'msg':'ID is mandatory for Deletion Operation, please provide ID'})
            return self.render_to_http_response(json_data)
        stu = self.get_object_by_id(id)
        if stu is None:
            json_data = json.dumps({'msg':'Given ID is Not Matched With exsiting record, Please Give some valid ID'})
            return self.render_to_http_response(json_data)
        status, delete_items = stu.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Record Deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'Unable to delete record.....please try again'})
        return self.render_to_http_response(json_data)
