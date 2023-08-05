from django.db import models

# Create your models here.
class Costfinder(models.Model):
    area = models.IntegerField()

    class Meta:
        verbose_name_plural = "Costfinder"

    # def __str__(self):
    #     return self # You can customize this as needed