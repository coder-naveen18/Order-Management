from django.contrib import admin
from .models import request_order

# Register your models here.
@admin.register(request_order)
class requestAdmin (admin.ModelAdmin):
    list_display = ('name', 'phone', 'items')