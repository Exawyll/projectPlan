from django.db import models

from projet.Models.resource import Resource


class Tache(models.Model):
    name = models.CharField(max_length=100)
    charge = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    resources = models.ManyToManyField(Resource)
    nb_resources = models.IntegerField(null=0)