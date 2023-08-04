from django.db import models

# Create your models here.
class Piechart(models.Model):
    area = models.FloatField(max_length=300)