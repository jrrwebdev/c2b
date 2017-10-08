from django.contrib import admin
from core.models import Customer, Category, BuyEvent

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'is_customer']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category)
admin.site.register(BuyEvent)
