from django.shortcuts import render

# Create your views here.
def seismologic(request):
    tab_title = "Seismologic"
    return render(request,'underconstructionTP.html',{"tab_title":tab_title})