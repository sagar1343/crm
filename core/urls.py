from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("agents/", views.agents, name="agents"),
    path("agents/<int:id>/edit", views.edit_agent, name="edit-agent"),
    path("properties/", views.properties, name="properties"),
    path("properties/<int:id>/edit", views.edit_property, name="edit-property"),
    path("leads/", views.leads, name="leads"),
    path("leads/<int:id>/edit", views.edit_lead, name="edit-lead"),
    path("deals/", views.deals, name="deals"),
    path("deals/<int:id>/edit", views.edit_agent, name="edit-deal"),
]
