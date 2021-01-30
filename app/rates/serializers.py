from rest_framework import serializers

from core.models import Rate


class RateSerializer(serializers.ModelSerializer):
    """Serializer for rate object"""

    class Meta:
        model = Rate
        fields = '__all__'
        read_only_Fields = ('id',)