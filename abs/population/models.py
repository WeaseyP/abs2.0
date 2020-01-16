from django.db import models

# Create your models here.

class Years(models.Model):
    years = models.PositiveSmallIntegerField()

class Australia(models.Model):
    australia_years = models.PositiveIntegerField()
    auspop_male = models.PositiveIntegerField()
    auspop_female = models.PositiveIntegerField()
    auspop = models.PositiveIntegerField()

class Aus_Births(models.Model):
    aus_birth_years = models.PositiveIntegerField()
    aus_births = models.PositiveIntegerField()

class Capital_Cities(models.Model):
    capital_years = models.PositiveIntegerField() 
    sydney_pop = models.PositiveIntegerField()
    melbourne_pop = models.PositiveIntegerField()
    brisbane_pop = models.PositiveIntegerField()
    adelaide_pop = models.PositiveIntegerField()
    perth_pop = models.PositiveIntegerField()
    hobart_pop = models.PositiveIntegerField()
    darwin_pop = models.PositiveIntegerField()
    canberra_pop = models.PositiveIntegerField()
    capital_cities = models.PositiveIntegerField()
    rest_nsw = models.PositiveIntegerField()
    rest_vic = models.PositiveIntegerField()
    rest_qld = models.PositiveIntegerField()
    rest_sa = models.PositiveIntegerField()
    rest_wa = models.PositiveIntegerField()
    rest_tas = models.PositiveIntegerField()
    rest_nt = models.PositiveIntegerField()
    rest_act = models.PositiveIntegerField()
    rest_states = models.PositiveIntegerField()

class States(models.Model):
    states_years = models.PositiveIntegerField()
    nsw_pop = models.PositiveIntegerField()
    vic_pop = models.PositiveIntegerField()
    qld_pop = models.PositiveIntegerField()
    sa_pop = models.PositiveIntegerField()
    wa_pop = models.PositiveIntegerField()
    tas_pop = models.PositiveIntegerField()
    nt_pop = models.PositiveIntegerField()
    act_pop = models.PositiveIntegerField()