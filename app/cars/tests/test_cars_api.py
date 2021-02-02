from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Car

from cars.serializers import CarSerializer


CARS_URL = reverse('car-list')


class PublicCarsApiTests(TestCase):
    """Test the publicly available cars API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_cars(self):
        res = self.client.get(CARS_URL)

        cars = Car.objects.all().order_by("id")
        serializer = CarSerializer(cars, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)