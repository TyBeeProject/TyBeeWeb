# coding: utf-8
from django.contrib import admin
from .models import Hive, Captor, Data
# Possibilité ajout capteur :
#    ajoute dans la bdd une table pour le nouveau capteur, ainsi que l'identifiant qui devra être utilisé pour parser le flux de la ruche
#
admin.site.register(Hive)
admin.site.register(Captor)
admin.site.register(Data)

# Possibilité ajout ruche :
#    ajoute une adresse ip/ un port pour la ruche nouvelle ruche à contacter
