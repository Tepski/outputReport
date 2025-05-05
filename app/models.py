from django.db import models

# Create your models here.

class MachineData(models.Model):
    machine = models.IntegerField()
    date = models.CharField(max_length=40)
    shift = models.CharField(max_length=2, null=True)
    ds_ok_count = models.IntegerField(null=True)
    ds_ng_count = models.IntegerField(null=True)
    ns_ok_count = models.IntegerField(null=True)
    ns_ng_count = models.IntegerField(null=True)
    ds_ok_perhr = models.CharField(null=True, max_length=200)
    ds_ng_perhr = models.CharField(null=True, max_length=200)
    ns_ok_perhr = models.CharField(null=True, max_length=200)
    ns_ng_perhr = models.CharField(null=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SAM {self.machine}"