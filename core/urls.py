from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("agents/", views.agents, name="agents"),
    path("agents/<int:id>/edit", views.edit_agent, name="edit-agent"),
    path("agents/<int:id>/delete", views.delete_agent, name="delete-agent"),
    path("properties/", views.properties, name="properties"),
    path("properties/<int:id>/edit", views.edit_property, name="edit-property"),
    path("properties/<int:id>/delete", views.delete_property, name="delete-property"),
    path("leads/", views.leads, name="leads"),
    path("leads/<int:id>/edit", views.edit_lead, name="edit-lead"),
    path("leads/<int:id>/delete", views.delete_lead, name="delete-lead"),
    path("leads/<int:id>/status", views.update_lead_status, name="update-lead-status"),
    path("deals/", views.deals, name="deals"),
    path("deals/<int:id>/edit", views.edit_deal, name="edit-deal"),
    path("deals/<int:id>/delete", views.delete_deal, name="delete-deal"),
]
