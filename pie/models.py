from django.db import models

# Create your models here.
class Costfinder(models.Model):
    area = models.FloatField(max_length=300)

    class Meta:
        verbose_name_plural = "Costfinder"