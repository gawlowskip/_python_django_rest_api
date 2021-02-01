from rest_framework import viewsets, mixins
from django.db.models import Avg, F, Value
from django.db.models.functions import Coalesce

from core.models import Car

from cars import serializers


class CarViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage cars in the database"""
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer

    def get_queryset(self):
        """Get all cars"""
        return self.queryset.order_by('id').annotate(rating=Coalesce(Avg(F('rate__rate')), Value(0)))

    def perform_create(self, serializer):
        """Create new car"""
        serializer.save()


class PopularCarViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Show popular cars"""
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer

    def get_queryset(self):
        """Get all popular cars"""
        return self.queryset.order_by('id').annotate(rating=Coalesce(Avg(F('rate__rate')), Value(0)))