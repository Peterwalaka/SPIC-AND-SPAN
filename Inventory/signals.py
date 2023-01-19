from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from Inventory.models import EquipmentAssignment


@receiver(post_save, sender=EquipmentAssignment, dispatch_uid="update_equipments_quantity")
def update_equipments_quantity(sender, instance, created, **kwargs):
    if created:
        equipment = instance.equipment
        equipment.quantity -= instance.quantity
        equipment.save()
