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
    context = {'hives': hives}
    return render(request, 'monitoring/seeHives.html', context)

    
def seeHive(request, idHive = 1):
    try:
        hive = Hive.objects.get(id = int(idHive))
        captors = hive.captor_set.all()
    except Hive.DoesNotExist:
        # todo : raise a better 404
        return HttpResponse(status = 404)
    
    # For each captors :
    charts = []
    for captor in captors:        
        charts.append(captor.formatDatas(2, 24))
                
    context = {'hive': hive, 'captors': captors, 'charts': charts}
    return render(request, 'monitoring/seeHive.html', context)


def seeCaptor(request, idHive = 1, idCaptor = 1):
    try:
        hive = Hive.objects.get(id = int(idHive))
        captor = hive.captor_set.get(id = int(idCaptor))        
    except Hive.DoesNotExist:
        # todo : raise a better 404
        return HttpResponse(status = 404)

    chart = captor.formatDatas(24, 24*10)
    context = {'hive': hive, 'captors': captors, 'chart': chart}
    return render(request, 'monitoring/seeCaptor.html', context)
