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
        """Test retrieving list of cars"""
        res = self.client.get(CARS_URL)

        cars = Car.objects.all().order_by("id")
        serializer = CarSerializer(cars, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_car_successfully(self):
        """Test creating a new car"""
        payload = {'make': 'Honda', 'model': 'Accord'}
        res = self.client.post(CARS_URL, payload)

        exists = Car.objects.filter(
            make=payload['make'],
            model=payload['model']
        ).exists()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)
