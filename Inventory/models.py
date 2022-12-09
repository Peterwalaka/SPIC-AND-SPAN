from django.db import models

# Create your models here.

class InventoryAccount(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class InventoryTransaction(models.Model):
    account = models.ForeignKey(InventoryAccount, on_delete=models.CASCADE, related_name="transactions")
    created_on = models.DateTimeField(auto_now_add=True)
    equipment_no = models.ImageField()

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        setattr(self, "_original_equipment_no", getattr(self, "equipment_no"))








