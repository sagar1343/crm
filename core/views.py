from django.shortcuts import render
from .models import Agent, Property, Lead, Deal
from .forms import AgentForm, DealForm, LeadForm, PropertyForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def agents(request):
    form = AgentForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    queryset = Agent.objects.all()
    context = {"agents": queryset, "form": AgentForm()}
    return render(request, "pages/agents.html", context)


def properties(request):
    form = PropertyForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    queryset = Property.objects.all()
    context = {"properties": queryset, "form": PropertyForm()}
    return render(request, "pages/properties.html", context)


def leads(request):
    form = LeadForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    queryset = Lead.objects.all()
    context = {"leads": queryset, "form": LeadForm()}
    return render(request, "pages/leads.html", context)


def deals(request):
    form = DealForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    queryset = Deal.objects.all()
    context = {"deals": queryset, "form": DealForm()}
    return render(request, "pages/deals.html", context)
