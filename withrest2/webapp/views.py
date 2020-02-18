from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from webapp.serializers import NameSerializers
# Create your views here.

class TestApiView(APIView):
    def get(self, request,*args,**kwargs):
        color =['RED', 'YELLOW','BLACK', 'BLUE']
        return Response({'msg':color})

    def post(self,request,*args,**kwargs):
        serializer = NameSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg ="Happy New Year {}".format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors)

    def put(self, request,*args,**kwargs):
        return Response({'msg':'This from put method'})

    def patch(self, request,*args,**kwargs):
        return Response({'msg':'This from patch method'})

    def delete(self, request,*args,**kwargs):
        return Response({'msg':'This from delete method'})

from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self, request):
        color =['RED', 'YELLOW','BLACK', 'BLUE']
        return Response({'msg':color})
    def create(self, request):
        serializer = NameSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg ="Happy New Year {}".format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors)
    def retrieve(self,request, pk = None):
        return Response({'msg':'This from retrieve method'})

    def update(self,request, pk = None):
        return Response({'msg':'This from update method'})

    def partial_update(self,request, pk = None):
        return Response({'msg':'This from partial_update method'})

    def destroy(self,request, pk = None):
        return Response({'msg':'This from destroy method'})
