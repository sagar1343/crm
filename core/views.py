from django.shortcuts import render
from .models import Agent, Property, Lead


# Create your views here.
def home(request):
    return render(request, "home.html")


def agents(request):
    queryset = Agent.objects.all()
    context = {"agents": queryset}
    return render(request, "pages/agents.html", context)


def properties(request):
    queryset = Property.objects.all()
    context = {"properties": queryset}
    return render(request, "pages/properties.html", context)


def leads(request):
    queryset = Lead.objects.all()
    context = {"leads": queryset}
    return render(request, "pages/leads.html", context)


def deals(request):
    return render(request, "pages/deals.html")
