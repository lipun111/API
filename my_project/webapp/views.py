from django.shortcuts import render
from .models import Template
from webapp.serializers import TemplateSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
# Create your views here.

class TemplateApiView(APIView):
    serializer_class = TemplateSerializers

    def get(self, request, *args, **kwargs):
        queryset = Template.objects.all()
        serializer = TemplateSerializers(queryset,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TemplateSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Save Data'})
        else:
            return Response(serializer.error,{'msg':'Error'})
