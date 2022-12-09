from django.contrib import admin
from .models import Category
from .models import Product






class SellAdmin(admin.ModelAdmin):
    list_display=('category', 'title', 'description', 'thumbnail', 'location','address', 'price', 'negotiable', 'phone_number', 'name',)
    
    


admin.site.register(Category)
admin.site.register(Product)



#admin.site.register(Sell, SellAdmin)