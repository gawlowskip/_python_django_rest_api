import requests

from requests.utils import requote_uri
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
        make = attrs.get('make').upper()
        model = attrs.get('model').upper()
        url = requote_uri(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json")

        response = requests.get(url)
        results = response.json().get('Results')

        cars = [car for car in results if car['Make_Name'].upper() == make]
        if not cars:
            raise serializers.ValidationError("Car make is invalid")

        model = [car for car in results if car['Model_Name'].upper() == model]
        if not model:
            raise serializers.ValidationError("Car model is invalid")

        return attrs