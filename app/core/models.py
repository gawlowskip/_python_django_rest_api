from django.db import models


class Car(models.Model):
    """
    Car to be used in app
    """
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name