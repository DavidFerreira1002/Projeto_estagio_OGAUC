from django.db import models

# Create your models here.
class Meteo_24h(models.Model):
    timestamp = models.CharField(max_length=20,null=True)
    temp_avg = models.FloatField(null=True)
    temp_max = models.FloatField(null=True)
    temp_min = models.FloatField(null=True)
    hrel_avg = models.FloatField(null=True)
    pressao_avg = models.FloatField(null=True)
    pnmm_avg = models.FloatField(null=True)
    precip_tot = models.FloatField(null=True)

    def __str__(self):
        return self.timestamp