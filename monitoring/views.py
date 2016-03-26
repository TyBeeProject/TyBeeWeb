from django.shortcuts import render
from django.http import HttpResponse

from .models import Hive, Captor, Data

import json


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


def seeHive(request, idHive = 0):
    try:
        hive = Hive.objects.get(id = int(idHive))
    except Hive.DoesNotExist:
        # todo : raise a better 404
        return HttpResponse(status = 404)
    
    # For each captors :
    charts = []
    for captor in hive.captor_set.all():
        ident = captor.id
        name = captor.name
        datas = [[[data.timeStamp,data.value] for data in captor.data_set.all()]]
        
        yaxis = '{max: 100, min: 0, zoomRange: [0.1, 100], panRange : [0,100]}'
        xaxis = ' {zoomRange: [0.1, 100], panRange: [0, '+ str(max([d[0] for d in datas]))+'] }'
        opts = '{ yaxis :'+yaxis +', xaxis :'+ xaxis+', zoom : {interactive : true}, pan : { interactive : true} }'

        chart = {'datas': str(datas), 'id':ident, 'options': opts, 'name': name}
        
        charts.append(chart)
        
    # chart = {'datas':str(charts), 'options':'{ yaxis : {max: 100}, xaxis: { zoomRange: [0.1, 100], panRange: [0, '+max([str(chart[0]) for chart in charts[0]])+'] }, yaxis: { zoomRange: [0.1, 100], panRange: [0, 100] }, zoom: { interactive: true },	pan: { interactive: true }}', 'id': 'A'}
        
    context = {'charts': charts}#, 'debug':debug}
    return render(request, 'monitoring/seeHive.html', context)

