from django.db import models

class Dam(models.Model):
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)

    def  __str__(self):
        return self.name

class DamStatistics(models.Model):
    dam = models.ForeignKey(Dam, on_delete=models.CASCADE, related_name='statistics')
    date = models.DateField()
    rainfall = models.FloatField()
    inflow = models.FloatField()
    power_house_discharge = models.FloatField()
    spillway_release = models.FloatField()

    class Meta:
        unique_together = ('dam', 'date')

    def _str_(self):
        return f'{self.dam.name} - {self.date}'