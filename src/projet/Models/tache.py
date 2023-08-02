from django.db import models


class Tache(models.Model):
    name = models.CharField(max_length=100)
    charge = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()