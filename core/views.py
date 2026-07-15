from django.shortcuts import render
from .models import Agent, Property


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
    return render(request, "pages/leads.html")


def deals(request):
    return render(request, "pages/deals.html")
