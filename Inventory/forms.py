from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm, ModelChoiceField

from Inventory.models import Equipment, EquipmentAssignment
from Inventory.selectors import get_equipment_list

User: AbstractUser = get_user_model()


class EquipmentModelForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'quantity', 'type']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name.lower()


class EquipmentAssignmentModelForm(ModelForm):
    equipment = ModelChoiceField(queryset=get_equipment_list(), empty_label="Select equipment")
    assigned = ModelChoiceField(queryset=User.objects.all(), empty_label="Select assigned user")

    class Meta:
        model = EquipmentAssignment
        exclude = ['assigner', 'tallied', 'status']

    def clean(self):
        cleaned_data = super(EquipmentAssignmentModelForm, self).clean()
        quantity = cleaned_data.get('quantity')
        equipment = cleaned_data.get('equipment')
        if quantity > equipment.quantity:
            self.add_error('quantity', f"Sorry only {equipment.quantity} {equipment.name} are available")
        return cleaned_data
