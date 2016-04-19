Frontend Web du projet TyBee
============================

Le projet TyBee est un projet de ruche connectée, sur le campus de Télécom Bretagne (Brest),
il s'inscrit dans le cadre des projets developpement durable du S2.

Ce repo contient le frontend web du projet, consitant en une application web affichant le monitorage des capteurs connectés à la ruche.

# Spec

Le projet est un site poussé par le framework Django.


## Mise en place

Vous aurez besoin de python3, pip, virtualenv et git
Il est conseillé de créer un virtualenv python3 pour ne pas faire interférer votre installation python avec l'application.

```
pip3 install virtualenv
virtualenv -p `whereis python3` TyBee
cd TyBee
source bin/activate
git clone https://github.com/TyBeeProject/TyBeeWeb
pip install -r TyBeeWeb/requirements.txt
```

Ensuite vous pouvez tester via le debug de Django

```
cd TyBeeWeb
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Puis naviguer sur 127.0.0.1:8000

Pour le déploiement, je vous laisse faire tout seul comme des grands ;)


# Contact

Le projet est réalisé par :

 -  Loïc Carr
 -  Thomas Delaby
 -  Ladislas Ducerf
 -  Xavier Duquesne
 -  Jihad Hamzi
 -  Juliette Homassel
 -  Théo Jacquin
 -  Agathe Villien
