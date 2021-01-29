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

    def validate(self, attrs):
        """
        Check that the make and model are valid
        """
        response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{attrs.get('make').upper()}?format=json")
        results = response.json().get('Results')

        if not results:
            raise serializers.ValidationError("Car make is invalid")

        model = [car for car in results if car['Model_Name'] == attrs.get('model')]

        if not model:
            raise serializers.ValidationError("Car model is invalid")

        return attrs