from django.shortcuts import render
from django.http import HttpResponse

from .models import Hive, Captor, Data

import json
import time

# Affichage capteur, choix chronologie etc
def putDatas(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        datas = json.loads(body_unicode)

        ts = datas['timeStamp']
        try:
            hive = Hive.objects.get(id=int(datas['idHive']))
        except Hive.DoesNotExist :
            #log something
            return HttpResponse (status = 401)

        
        for data in datas['captorDatas']:
            try:
                captor = hive.captor_set.get(id=int(data[0]))
            except DoesNotExist :
                # We decide not to create automatically the captor
                return HttpResponse (status = 402)

            captor.addMeasure(ts, float(data[1]))

        return render(request, 'monitoring/putDatas.html')
    return HttpResponse (status = 401)


def seeHives(request):
    hives = Hive.objects.all()
    formattedHives = [
        {
            'id': hive.id,
            'name': hive.name,
            'photo': hive.photo,
            'shortDescription': hive.shortDescription,
            'description': hive.description,
            'graphs': [ captor.formatDatas(2,2) for captor in hive.captor_set.all()]
        }
        for hive in hives
    ]
    context = {'hives': formattedHives}
    return render(request, 'monitoring/seeHives.html', context)

    
def seeHive(request, idHive = 1):
    try:
        hive = Hive.objects.get(id = int(idHive))
    except Hive.DoesNotExist:
        # todo : raise a better 404
        return HttpResponse(status = 404)
    
    # For each captors :
    formattedHive = {
        'id': hive.id,
        'name': hive.name,
        'photo': hive.photo,
        'shortDescription': hive.shortDescription,
        'description': hive.description,
        'graphs': [ captor.formatDatas(2,24) for captor in hive.captor_set.all()]
    }

    context = {'hive': formattedHive}
    return render(request, 'monitoring/seeHive.html', context)


def seeCaptor(request, idHive = 1, idCaptor = 1):
    try:
        hive = Hive.objects.get(id = int(idHive))
        captors = hive.captor_set.all()
        captor = hive.captor_set.get(id = int(idCaptor))        
    except Hive.DoesNotExist:
        # todo : raise a better 404
        return HttpResponse(status = 404)

    chart = captor.formatDatas(24, 24*10)
    context = {'hive': hive, 'captors': captors, 'graph': chart}
    return render(request, 'monitoring/seeCaptor.html', context)
