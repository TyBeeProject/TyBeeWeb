from django.db import models

import time

class Hive (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__ (self):
        return self.name + " (" + str(self.id)+ ")"

    
class Captor (models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    #unit = models.ChoiceField()        # Permet de choisir l'unité de la donnée
    incertitude = models.FloatField()  # l'incertitude donnée du capteur

    #datas = models.Dictionnary
    
    def addMeasure(self, ts, val):
        newData = Data(captor = self, timeStamp = ts, value = val)
        newData.save()        
        self.save()

        
    def formatDatas(self, nbHoursFocus, nbHoursTotal):
        # We multiply timestamp by 1000 because unix's one count seconds whereas js' one count miliseconds.        
        datas = [[data.timeStamp*1000,data.value] for data in self.data_set.all()]
        maxX = max([d[0] for d in datas])
        maxY = max([d[1] for d in datas])
        initialMaxX = time.time()*1000
        initialMinX = initialMaxX - 1000*3600*nbHoursFocus
        minX = max(initialMaxX - 1000*3600*nbHoursTotal,0)

        # Determine the index to slice datas' values.
        for index in range(len(datas)-1,0,-1):
            if datas[index][0] < minX:                
                break

        formattedDatas = [datas[index:]]
        
        zoomMinX = 5
        
        yaxis = '{max: 100, min: 0, zoomRange: [100, 100], panRange : [0,100]}'
        xaxis = r'{mode: "time", timeformat: "%d/%m - %H:%M:%S", max: '+ str(initialMaxX) +', min: '+str(initialMinX) +', zoomRange: ['+ str(zoomMinX) +', null], panRange: ['+ str(minX) +', '+ str(maxX) +'] }'
        opts = '{ yaxis :'+yaxis +', xaxis :'+ xaxis+', zoom : {interactive : true}, pan : { interactive : true} }'

        chart = {'datas': str(formattedDatas), 'id':self.id, 'options': opts, 'name': self.name}

        return chart

    
    def __str__ (self):
        return self.name + " (" + str(self.id)+ ")"

    
class Data (models.Model):
    captor = models.ForeignKey(Captor, on_delete=models.CASCADE)
    timeStamp = models.FloatField()
    value = models.FloatField()
        
    def __str__ (self):
        return str(self.value) 
    
