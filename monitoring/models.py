# coding: utf-8
import time

from django.db import models


class Hive(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    shortDescription = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="img/hivePhotos", null=True)

    def __unicode__(self):
        return self.name + " (" + str(self.id) + ")"


class Captor(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    unit_choices = (
        ('kg', 'Kilogrammes'),
        ('dB', 'DéciBels'),
        ('dC', 'Degrés Celcius'),
        ('pct', 'Pourcentages'),
    )
    unit = models.CharField(max_length=3, choices=unit_choices)  # Permet de choisir l'unité de la donnée
    incertitude = models.FloatField()  # l'incertitude donnée du capteur
    reference = models.CharField(max_length=100)

    # datas = models.Dictionnary
    
    def addMeasure(self, ts, val):
        newData = Data(captor=self, timeStamp=ts, value=val)
        newData.save()        
        self.save()

    def formatDatas(self, nbHoursFocus, nbHoursTotal):
        # We multiply timestamp by 1000 because unix's one count seconds whereas js' one count miliseconds.        
        datas = [[data.timeStamp * 1000, data.value] for data in self.data_set.all()] or [[0, 0]]
        maxX = max([d[0] for d in datas])
        minX = min([d[0] for d in datas])
        maxY = max([d[1] for d in datas])

        initialMaxX = time.time() * 1000
        initialMinX = initialMaxX - 1000*3600*nbHoursFocus
        minX = max(initialMaxX - 1000 * 3600 * nbHoursTotal, minX)

        # Determine the index to slice datas' values.
        index = 0
        for index in range(len(datas) - 1, 0, -1):
            if datas[index][0] < minX:                
                break

        formattedDatas = [datas[index:]]

        zoomMinX = 5

        yaxis = '{max: 100, min: 0, zoomRange: [100, 100], panRange : [0,100]}'
        xaxis = r'{mode: "time", timeformat: "%d/%m - %H:%M", max: ' + str(initialMaxX) + ', min: ' + str(
            initialMinX) + ', zoomRange: [' + str(zoomMinX) + ', null], panRange: [' + str(minX) + ', ' + str(
            maxX) + '] }'
        opts = '{ yaxis :' + yaxis + ', xaxis :' + xaxis + ', zoom : {interactive : true}, pan : { interactive : true} }'

        chart = {'datas': str(formattedDatas), 'id': self.id, 'options': str(opts), 'name': self.name,
                 'reference': self.reference, 'unit': self.unit, 'incertitude': self.incertitude}

        return chart

    def __unicode__(self):
        return self.name + " (" + str(self.id) + ")"


class Data(models.Model):
    captor = models.ForeignKey(Captor, on_delete=models.CASCADE)
    timeStamp = models.FloatField()
    value = models.FloatField()

    def __unicode__(self):
        return str(self.value) 
