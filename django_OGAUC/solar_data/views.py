from django.shortcuts import render
from .models import Solar_image
from django.db.models import Q
from django.core import serializers
import json
import os

# Create your views here.
def solar(request):
    tab_title = "Solar Data"

    class Solarimages:
        def __init__(self,HA,HAZ,CN,DOP,K1,K3,CNspots,K3fac):
                super().__init__()
                self.HA = HA
                self.HAZ = HAZ
                self.CN = CN
                self.DOP = DOP
                self.K1 = K1
                self.K3 = K3
                self.CNspots = CNspots
                self.K3fac = K3fac

    ordered = Solar_image.objects.order_by('-date')
    earliest = ordered.first()
    solar_data_HA = earliest.HA_image
    solar_data_HAZ = earliest.HAZ_image
    solar_data_CN = earliest.CN_image
    solar_data_DOP = earliest.DOP_image
    solar_data_K1 = earliest.K1_image
    solar_data_K3 = earliest.K3_image
    solar_data_CNspots = earliest.CNspots_image
    solar_data_K3fac = earliest.K3fac_image
    solar_data =Solarimages(HA=solar_data_HA,HAZ=solar_data_HAZ,CN=solar_data_CN,DOP=solar_data_DOP,K1=solar_data_K1,K3=solar_data_K3,CNspots=solar_data_CNspots,K3fac=solar_data_K3fac)
    print(solar_data.HA)

    return render(request,'Solar/solarTP.html',{"tab_title":tab_title,"solar_images":solar_data})