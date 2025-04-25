from django.contrib import admin
from . models import MachineData
# Register your models here.

class MachineDataAdmin(admin.ModelAdmin):
    list_display = ["machine", "date", "ds_ok_count", "ds_ng_count", "ns_ok_count", "ns_ng_count"];

admin.site.register(MachineData, MachineDataAdmin)

