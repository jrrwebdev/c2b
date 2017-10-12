from django.contrib import admin
from core.models import Customer, BuyEvent, Category

# Register your models here.
admin.site.register(Customer)
admin.site.register(BuyEvent)
admin.site.register(Category)
