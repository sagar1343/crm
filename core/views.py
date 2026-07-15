from django.shortcuts import render
from .models import Agent, Property, Lead, Deal
from .forms import AgentForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def agents(request):
    form = AgentForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    queryset = Agent.objects.all()
    context = {"agents": queryset, "form": form}
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
    queryset = Deal.objects.all()
    context = {"deals": queryset}
    return render(request, "pages/deals.html", context)
