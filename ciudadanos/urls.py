from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CiudadanoViewSet

router = DefaultRouter()
router.register(r'ciudadanos', CiudadanoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
