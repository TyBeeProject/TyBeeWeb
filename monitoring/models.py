from django.db import models

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
        
    def __str__ (self):
        return self.name + " (" + str(self.id)+ ")"

    
class Data (models.Model):
    captor = models.ForeignKey(Captor, on_delete=models.CASCADE)
    timeStamp = models.FloatField()
    value = models.FloatField()
        
    def __str__ (self):
        return str(self.value) 
    
