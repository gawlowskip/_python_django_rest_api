from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cars import views


router = DefaultRouter()
router.register('', views.CarViewSet)
router.register('/popular', views.PopularCarViewSet)

urlpatterns = [
    path('', include(router.urls))
]