from django.shortcuts import render

# Create your views here.
def geomagnetic(request):
    tab_title = "Geomagnetic Data"
    return render(request,'Geomagnetic/geomagneticTP.html',{"tab_title":tab_title})

def coistation(request):
    tab_title = "COI Station"
    return render(request,'Geomagnetic/coistationTP.html',{"tab_title":tab_title})

def hdzcomponents(request):
    tab_title = "HDZ Components"
    return render(request,'Geomagnetic/hdzcomponentsTP.html',{"tab_title":tab_title})

def shorttermvariability(request):
    tab_title = "Short Term Variability"
    return render(request,'Geomagnetic/shorttermvariabilityTP.html',{"tab_title":tab_title})

def dailyvariation(request):
    tab_title = "Daily Variation"
    return render(request,'Geomagnetic/dailyvariationTP.html',{"tab_title":tab_title})

def localkindices(request):
    tab_title = "Local K Indices"
    return render(request,'Geomagnetic/localkindicesTP.html',{"tab_title":tab_title})

def monthlyreport(request):
    tab_title = "Monthly Report"
    return render(request,'Geomagnetic/monthlyreportTP.html',{"tab_title":tab_title})