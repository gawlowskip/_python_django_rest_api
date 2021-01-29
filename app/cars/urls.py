from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cars import views


router = DefaultRouter()
router.register('', views.CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]