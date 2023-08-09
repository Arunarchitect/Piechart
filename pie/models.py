from django.db import models
from django.core.validators import MinValueValidator

class Costfinder(models.Model):
    area = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='default/image.png', default='image.png')

    class Meta:
        verbose_name_plural = "Costfinder"
