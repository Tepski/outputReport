from django.db import models

# Create your models here.

class MachineData(models.Model):
    machine = models.IntegerField()
    date = models.CharField(max_length=40)
    shift = models.CharField(max_length=2, null=True, default="DS")
    ds_ok_count = models.IntegerField(null=True, default=0)
    ds_ng_count = models.IntegerField(null=True, default=0)
    ns_ok_count = models.IntegerField(null=True, default=0)
    ns_ng_count = models.IntegerField(null=True, default=0)
    ds_ok_perhr = models.CharField(null=True, max_length=200, default="[]")
    ds_ng_perhr = models.CharField(null=True, max_length=200, default="[]")
    ns_ok_perhr = models.CharField(null=True, max_length=200, default="[]")
    ns_ng_perhr = models.CharField(null=True, max_length=200, default="[]")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SAM {self.machine}"