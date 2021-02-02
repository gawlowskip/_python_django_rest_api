from django.contrib import admin

from core.models import Car


class CarAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'make', 'model', 'created_at', 'updated_at']

    def save_model(self, request, obj, form, change):
        # TODO: Add validation for make and model
        super(CarAdmin, self).save_model(request, obj, form, change)


admin.site.register(Car, CarAdmin)
