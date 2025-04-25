from rest_framework import serializers
from . models import MachineData

class MachineSrlzr(serializers.ModelSerializer):
    class Meta:
        model = MachineData
        fields = "__all__"