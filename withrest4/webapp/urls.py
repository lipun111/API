from rest_framework.routers import DefaultRouter
from webapp import views

router = DefaultRouter()
router.register('api', views.EmployeeViewSetCRUD)
urlpatterns = router.urls
