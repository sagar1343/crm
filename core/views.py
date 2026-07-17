from django.shortcuts import render, get_object_or_404, redirect
from .models import Agent, Property, Lead, Deal
from .forms import AgentForm, DealForm, LeadForm, PropertyForm, EditAgentForm
from django.views.decorators.http import require_POST
from django.db.models import Sum, F
from django.utils import timezone


# Create your views here.
def dashboard(request):
    result = Deal.objects.filter(status=Deal.DealStatus.DONE).aggregate(
        total=Sum("amount")
    )
    total_deals = (
        Deal.objects.filter(status=Deal.DealStatus.DONE)
        .filter(actual_closing_date__year=timezone.now().year)
        .filter(actual_closing_date__month=timezone.now().month)
        .count()
    )
    total_agents = Agent.objects.count()
    total_leads = (
        Lead.objects.filter(created_at__year=timezone.now().year)
        .filter(created_at__month=timezone.now().month)
        .count()
    )

    done_deals = Deal.objects.filter(
        status=Deal.DealStatus.DONE
    ).select_related("lead__assigned_agent")
    net_profit = sum(
        (d.amount * d.commission_percent / 100)
        * (100 - d.lead.assigned_agent.commission_share)
        / 100
        for d in done_deals
    )
    print(net_profit)

    sold_properties = Property.objects.filter(status=Property.Status.SOLD).count()
    context = {
        "total_sale": result["total"],
        "total_deals": total_deals,
        "total_agents": total_agents,
        "total_leads": total_leads,
        "sold_properties": sold_properties,
        "profit": net_profit,
    }
    return render(request, "home.html", context)


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
    context = {
        "leads": queryset,
        "form": LeadForm(),
        "lead_statuses": Lead.LeadStatus.choices,
    }
    return render(request, "pages/leads.html", context)


def deals(request):
    form = DealForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    queryset = Deal.objects.all()
    context = {"deals": queryset, "form": DealForm()}
    return render(request, "pages/deals.html", context)


def edit_agent(request, id):
    instance = get_object_or_404(Agent, id=id)
    form = EditAgentForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("agents")

    context = {"editform": form, "id": id}
    return render(request, "pages/editagent.html", context)


def edit_property(request, id):
    instance = get_object_or_404(Property, id=id)
    form = PropertyForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("properties")

    context = {"editform": form, "id": id}
    return render(request, "pages/editproperty.html", context)


def edit_lead(request, id):
    instance = get_object_or_404(Lead, id=id)
    form = LeadForm(request.POST or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("leads")

    context = {"editform": form, "id": id}
    return render(request, "pages/editleads.html", context)


def edit_deal(request, id):
    instance = get_object_or_404(Deal, id=id)
    form = DealForm(request.POST or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("deals")

    context = {"editform": form, "id": id}
    return render(request, "pages/editdeal.html", context)


@require_POST
def delete_deal(request, id):
    instance = get_object_or_404(Deal, id=id)
    instance.delete()
    return redirect("deals")


@require_POST
def delete_agent(request, id):
    instance = get_object_or_404(Agent, id=id)
    instance.delete()
    return redirect("agents")


@require_POST
def delete_lead(request, id):
    instance = get_object_or_404(Lead, id=id)
    instance.delete()
    return redirect("leads")


@require_POST
def delete_property(request, id):
    instance = get_object_or_404(Property, id=id)
    instance.delete()
    return redirect("properties")


@require_POST
def update_lead_status(request, id):
    status = request.POST.get("status")
    instance = get_object_or_404(Lead, id=id)
    instance.status = status
    instance.save()
    return redirect("leads")
