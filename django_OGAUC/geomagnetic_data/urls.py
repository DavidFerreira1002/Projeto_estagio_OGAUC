from django.urls import path 
from . import views
urlpatterns = [
   path("",views.geomagnetic,name="geomagnetic"),
   path("coistation",views.coistation,name="coistation"),
   path("hdzcomponents",views.hdzcomponents,name="hdzcomponents"),
   path("shorttermvariability",views.shorttermvariability,name="shorttermvariability"),
   path("dailyvariation",views.dailyvariation,name="dailyvariation"),
   path("localkindices",views.localkindices,name="localkindices"),
   path("monthlyreport",views.monthlyreport,name="monthlyreport") 
]