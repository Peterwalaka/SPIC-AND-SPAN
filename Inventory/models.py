from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class InventoryAccount(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class InventoryTransaction(models.Model):
    account = models.ForeignKey(InventoryAccount, on_delete=models.CASCADE, related_name="transactions")
    created_on = models.DateTimeField(auto_now_add=True)
    equipment_no = models.ImageField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        setattr(self, "_original_equipment_no", getattr(self, "equipment_no"))


User: AbstractUser = get_user_model()


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Equipment(TimestampModel):
    class Type(models.TextChoices):
        HARDWARE_EQUIPMENT = 'HE', _('Hardware Equipment')
        USABLE_EQUIPMENT = 'UE', _('Usable Equipment')

    name = models.CharField(max_length=250, unique=True)
    quantity = models.IntegerField(default=0)
    type = models.CharField(max_length=5, choices=Type.choices, default=Type.HARDWARE_EQUIPMENT)

    def __str__(self):
        return str(self.name)


class EquipmentAssignment(TimestampModel):
    class Status(models.TextChoices):
        ASSIGNED = 'AS', _('Assigned')
        RETURNED = 'RD', _('Returned')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_equipments")
    assigner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="equipments_given", null=True)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.ASSIGNED)
    tallied = models.BooleanField(default=False)


