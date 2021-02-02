from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rates import views


router = DefaultRouter()
router.register('', views.RateViewSet)

urlpatterns = [
    path('', include(router.urls))
]
