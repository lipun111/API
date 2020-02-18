from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('team', views.TeamView)
urlpatterns = [
    path('', include(router.urls)),
]
