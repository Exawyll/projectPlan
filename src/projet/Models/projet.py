from django.db import models

from projet.Models.tache import Tache


class Projet(models.Model):
    date_debut = models.DateField()
    taches = models.ManyToOneRel(Tache)