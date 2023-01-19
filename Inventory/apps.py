from django.apps import AppConfig


class InventoryConfig(AppConfig):
    name = 'Inventory'

    def ready(self):
        import Inventory.signals
