import requests
import logging
from rest_framework import serializers

from core.models import Car


class CarSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Car
        fields = '__all__'
        read_only_Fields = ('id',)

    def validate_make(self, value):
        """
        Check that the make is valid
        """
        response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{value.upper()}?format=json")
        results = response.json().get('Results')

        if not results:
            raise serializers.ValidationError("Car make does not exists")

        return value