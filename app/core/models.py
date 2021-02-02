from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    """
    Car to be used in app
    """
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model}"


class Rate(models.Model):
    """
    Rate to be used for car objects
    """
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                   MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
