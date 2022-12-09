from django.contrib import admin
from .models import InventoryAccount, InventoryTransaction

# Register your models here.

class InventoryTransactionInline(admin.TabularInline):
    model = InventoryTransaction

@admin.register(InventoryAccount)
class InventoryAccountAdmin(admin.ModelAdmin):

    inlines = [InventoryTransactionInline]
