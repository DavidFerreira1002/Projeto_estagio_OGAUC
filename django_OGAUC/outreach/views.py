from django.shortcuts import render

# Create your views here.
def outreach(request):
    tab_title = "Outreach"
    return render(request,'underconstructionTP.html',{"tab_title":tab_title})

def glossary(request):
    tab_title = "Glossary"
    return render(request,'underconstructionTP.html',{"tab_title":tab_title})

def research(request):
    tab_title = "Research"
    return render(request,'underconstructionTP.html',{"tab_title":tab_title})

def contacts(request):
    tab_title = "Contacts"
    return render(request,'underconstructionTP.html',{"tab_title":tab_title})    

def links(request):
    tab_title = "Links"
    return render(request,'underconstructionTP.html',{"tab_title":tab_title})