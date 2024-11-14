from django.db import models

class sampleSoil(models.Model):
    sample = models.FloatField(blank=True)
    ph = models.FloatField(blank=True)
    organicMaterial = models.FloatField(blank=True)
    phosporo = models.FloatField(blank=True)
    potassium = models.FloatField(blank=True)
    na = models.FloatField(blank=True)
    ca = models.FloatField(blank=True)
    mg = models.FloatField(blank=True)
    al = models.FloatField(blank=True)
    hAl = models.FloatField(blank=True)
    cu = models.FloatField(blank=True)
    fe = models.FloatField(blank=True)
    mn = models.FloatField(blank=True)
    zn = models.FloatField(blank=True)
    pRem = models.FloatField(blank=True)
    emptyBecker1 = models.FloatField(blank=True)
    emptyBecker2 = models.FloatField(blank=True)
    claySilt = models.FloatField(blank=True)
    clay = models.FloatField(blank=True)
