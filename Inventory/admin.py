from typing import Iterable

from django.contrib import admin, messages
from django.utils.translation import ngettext

from Inventory.forms import EquipmentModelForm, EquipmentAssignmentModelForm
from Inventory.models import EquipmentAssignment, Equipment


def update_equipment_quantity_after_return(queryset: Iterable[EquipmentAssignment]) -> None:
    for instance in queryset:
        if not instance.tallied:
            equipment = instance.equipment
            equipment.quantity += instance.quantity
            instance.tallied = True
            equipment.save()
            instance.save()


@admin.action(description='Mark selected assigned equipment as returned')
def make_returned(modeladmin, request, queryset):
    updated = queryset.update(status="RD")
    update_equipment_quantity_after_return(queryset=queryset)
    modeladmin.message_user(request, ngettext(
        '%d Equipment has been marked as returned successfully.',
        '%d Equipments have been marked as returned successfully.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(EquipmentAssignment)
class EquipmentAssignmentAdmin(admin.ModelAdmin):
    form = EquipmentAssignmentModelForm
    add_form = EquipmentAssignmentModelForm
    list_display = ('equipment', 'assigned', 'quantity', 'status', 'created', 'updated')
    search_fields = ('equipment__name',)
    search_help_text = "Search by equipment name"
    list_filter = ('status', 'created', 'updated')
    actions = [make_returned]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    form = EquipmentModelForm
    add_form = EquipmentModelForm
    list_display = ('name', 'type', 'quantity', 'created', 'updated')
    search_fields = ('name',)
    search_help_text = "Search by name"
    list_filter = ('type', 'created', 'updated')
