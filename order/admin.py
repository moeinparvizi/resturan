from django.contrib import admin
from .models import orderDetail
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'count', 'price']

    class Meta:
        model = orderDetail

admin.site.register(orderDetail, ProductAdmin)
