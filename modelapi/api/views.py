from django.shortcuts import render
from .models import Team
from .serializers import TeamSerializers
from rest_framework import viewsets
# Create your views here.


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializers
