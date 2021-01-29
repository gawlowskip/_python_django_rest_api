from django.contrib import admin

from core.models import Car


class CarAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['make', 'model', 'created_at', 'updated_at']


admin.site.register(Car, CarAdmin)