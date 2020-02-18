from django.shortcuts import render
from webapp.models import Employee
from rest_framework.views import APIView
from webapp.serializers import EmployeeSerializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
#
# class EmployeeListApiView(ListAPIView):
#     # queryset = Employee.objects.alls()
#     serializer_class = EmployeeSerializers
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#         return qs
#
# class EmployeeCreateApiView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#
# class EmployeeRetrieveApiView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#     lookup_field = 'id'
#
#
# class EmployeeUpdateApiView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#     lookup_field = 'id'
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#     lookup_field = 'id'

#
# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers

#
# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#     lookup_field = 'id'

#
# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
#     lookup_field = 'id'




# class EmployeeApiView(APIView):
#     def get(self,request, format=None):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializers(qs, many=True)
#         return Response(serializer.data)

from rest_framework import mixins


class EmployeeListCreateModelMixinView(mixins.CreateModelMixin,ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def post(self,request,*args,**kwargs):
        return self.post(request, *args,**kwargs)


class EmployeeRetrieveUpdateDestroyModelMixinView(mixins.DestroyModelMixin,mixins.UpdateModelMixin,RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def put(self,request,*args,**kwargs):
        return self.update(request, *args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return self.partial_update(request, *args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args,**kwargs)
