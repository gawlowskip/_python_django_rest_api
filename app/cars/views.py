from rest_framework import viewsets, mixins

from core.models import Car

from cars import serializers


class CarViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage cars in the database"""
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer

    def get_queryset(self):
        """Get all cars"""
        return self.queryset.order_by('-id')

    def perform_create(self, serializer):
        """Create new car"""
        serializer.save()