from django import forms
from .models import Agent, Property, Lead, Deal


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = "__all__"
