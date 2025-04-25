from django.db import models

# Create your models here.

class MachineData(models.Model):
    machine = models.IntegerField()
    date = models.CharField(max_length=40)
    ds_ok_count = models.IntegerField()
    ds_ng_count = models.IntegerField()
    ns_ok_count = models.IntegerField()
    ns_ng_count = models.IntegerField()
    ds_ok_perhr = models.CharField(max_length=200)
    ds_ng_perhr = models.CharField(max_length=200)
    ns_ok_perhr = models.CharField(max_length=200)
    ns_ng_perhr = models.CharField(max_length=200)

    def __str__(self):
        return f"SAM {self.machine}"