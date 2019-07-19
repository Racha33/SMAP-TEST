from django.db import models
#from api import Consumer
# Create your models here.

class ConsumerAPP(models.Model):

    consumer = models.ForeignKey('api.Consumer', on_delete=models.CASCADE)


