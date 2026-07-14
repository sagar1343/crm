from django.contrib import admin
from .models import Agent, Lead, Property, Deal

# Register your models here.

admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(Property)
admin.site.register(Deal)
