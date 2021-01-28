from rest_framework import serializers

from core.models import Car


class CarSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'created_at', 'updated_at')
        read_only_Fields = ('id',)