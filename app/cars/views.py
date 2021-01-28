from rest_framework import viewsets, mixins

from core.models import Car

from cars import serializers


class CarViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage cars in the database"""
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer

    def get_queryset(self):
        return self.queryset.order_by('-make')