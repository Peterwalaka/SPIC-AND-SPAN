from typing import Iterable

from Inventory.models import Equipment, EquipmentAssignment


def get_equipment_list() -> Iterable[Equipment]:
    queryset = Equipment.objects.all()
    return queryset


def get_equipment_assignment_list() -> Iterable[EquipmentAssignment]:
    queryset = EquipmentAssignment.objects.all()
    return queryset
