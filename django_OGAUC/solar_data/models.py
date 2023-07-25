from django.db import models
import datetime
# Create your models here.

def timeNow():
    YMDHm = str(datetime.datetime.now())
    YMDHm = YMDHm[0:16].replace(':','-').replace(' ','-').replace('-','_')
    return YMDHm

class Solar_image(models.Model):
    HA_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    HAZ_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    CN_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    CNspots_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    DOP_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    K1_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    K3_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    K3fac_image = models.ImageField(upload_to='/'.join(['solarData',timeNow()]),null=True)
    date = models.CharField(max_length=20,default=timeNow(),null=True)

    def __str__(self):
        return (self.date)
