from django.db import models

class Receta(models.Model):
    
    nombre = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=300)
   
    def publish(self):
        self.save()



