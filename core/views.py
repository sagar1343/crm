from django.shortcuts import render
from .models import Agent


# Create your views here.
def home(request):
    return render(request, "home.html")


def agents(request):
    queryset = Agent.objects.all()
    context = {"agents": queryset}
    return render(request, "pages/agents.html", context)


def properties(request):
    return render(request, "pages/properties.html")


def leads(request):
    return render(request, "pages/leads.html")


def deals(request):
    return render(request, "pages/deals.html")
