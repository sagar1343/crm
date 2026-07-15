from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("agents/", views.agents, name="agents"),
    path("properties/", views.properties, name="properties"),
    path("leads/", views.leads, name="leads"),
    path("deals/", views.deals, name="deals"),
]
