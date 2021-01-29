from django.contrib import admin

from core.models import Rate


class RateAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['car', 'rate', 'created_at']


admin.site.register(Rate, RateAdmin)