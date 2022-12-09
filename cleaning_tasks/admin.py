from django.contrib import admin
from .models import FieldSupervisionTasks
from .models import CleaningTasks

# Register your models here.

admin.site.register(FieldSupervisionTasks)
admin.site.register(CleaningTasks)
