from django.contrib import admin
from core.models import Customer, BuyEvent, Category

class BuyEventAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('name', 'description', 'category', 'price', 'like', 'photo')

class CustomerAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('category','person_type', 'is_customer', 'first_name', 'last_name', 'address', 'city', 'state_province', 'country' , 'rg', 'cnpj', 'ie')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(BuyEvent, BuyEventAdmin)
admin.site.register(Category)
