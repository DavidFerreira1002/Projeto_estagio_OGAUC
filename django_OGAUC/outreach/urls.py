from django.urls import path
from . import views

urlpatterns = [
    path("",views.outreach,name="outreach"),
    path("glossary",views.glossary,name="glossary"),
    path("research",views.research,name="research"),
    path("contacts",views.contacts,name="contacts"),
    path("links",views.links,name="links")
]