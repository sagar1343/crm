from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to="profiles", default="profiles/default.jpg"
    )
    phone_number = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    commission_share = models.DecimalField(max_digits=4, decimal_places=2)
    monthly_target = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"agent:{self.user.username}"


class Property(models.Model):
    class ProperyType(models.TextChoices):
        APARTMENT = "apartment", "Apartment"
        VILLA = "villa", "Villa"
        COMMERCIAL = "commercial", "Commercial"
        PLOT = "plot", "Plot"

    class Status(models.TextChoices):
        AVAILABLE = "available", "Available"
        SOLD = "sold", "Sold"

    title = models.CharField(max_length=255)
    Description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    property_type = models.CharField(max_length=12, choices=ProperyType.choices)
    image = models.ImageField(upload_to="properties")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.AVAILABLE
    )
    listing_agent = models.ForeignKey(
        to=Agent, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    area_sqft = models.PositiveIntegerField()
    listed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lead(models.Model):
    class LeadStatus(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        SITE_VISITED = "site_visited", "Site Visited"
        NEGOTIATIONS = "negotiations", "Negotiations"
        LOST = "lost", "Lost"
        DONE = "done", "Done"

    class Source(models.TextChoices):
        WEBSITE = "website", "Website"
        REFERRAL = "referral", "Referral"
        WALKIN = "walkin", "Walkin"

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)
    source = models.CharField(max_length=12, choices=Source.choices)
    interested_property_types = models.CharField(max_length=255)
    min_budget = models.DecimalField(max_digits=12, decimal_places=2)
    max_budget = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=16, choices=LeadStatus.choices)
    assigned_agent = models.ForeignKey(to=Agent, on_delete=models.DO_NOTHING)
    preferred_location = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Deal(models.Model):
    class DealStatus(models.TextChoices):
        CANCELLED = "cancelled", "Cancelled"
        PENDING = "pending", "Pending"
        DONE = "done", "Done"

    lead = models.ForeignKey(to=Lead, on_delete=models.CASCADE)
    property = models.ForeignKey(to=Property, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=12, choices=DealStatus.choices, default=DealStatus.PENDING
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    expected_closing_date = models.DateField()
    actual_closing_date = models.DateField(null=True, blank=True)
    commission_percent = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property}:{self.lead}"
