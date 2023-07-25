from django.urls import path 
from . import views

urlpatterns = [
    path("",views.meteorologic,name="meteorologic"),
    path("insert24h",views.insert24h,name="insert24h")
]