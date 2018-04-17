from django.db import models
from django.utils.translation import ugettext_lazy as _


class Player(models.Model):
    CHOICES = (
        (0, "BATSMAN"),
        (1, "BOWLER"),
        (2, "ALL-ROUNDER"),
        (3, "WICKETKEEPER"),
    )
    name = models.CharField(_("Player Name"), max_length=254, unique=True)
    first_name = models.CharField(_("First Name"), max_length=254, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=254, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), blank=True, null=True)
    profile_image = models.URLField(_("Profile Image"), blank=True, null=True)
    country = models.CharField(_("Origin Country"), max_length=100, blank=True, null=True)
    specialism = models.IntegerField(_("Specialism"), choices=CHOICES, blank=True, null=True, default=0)


class IPLProfile(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    set_no = models.SmallIntegerField(blank=True, null=True)
    current_set = models.CharField(max_length=10, blank=True, null=True)
    matches = models.IntegerField(_("Matches Played"), blank=True, null=True)
    price = models.IntegerField(_("Reserve Price Rs Lakh"), blank=True, null=True)
