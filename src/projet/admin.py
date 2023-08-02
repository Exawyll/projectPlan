from django.contrib import admin

from projet.Models.resource import Resource
from projet.Models.tache import Tache

# Register your models here.
admin.site.register(Tache)
admin.site.register(Resource)