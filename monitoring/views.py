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
