from rest_framework import viewsets, mixins

from core.models import Rate

from rates import serializers


class RateViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """Manage rates in the database"""
    queryset = Rate.objects.all()
    serializer_class = serializers.RateSerializer

    def perform_create(self, serializer):
        """Create new rate"""
        serializer.save()
