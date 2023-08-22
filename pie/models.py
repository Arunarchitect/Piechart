from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Costfinder(models.Model):
    COST_CHOICES = [
        ('Ultra Low Cost', 'Ultra Low Cost'),
        ('Low Cost', 'Low Cost'),
        ('Medium', 'Medium'),
        ('Luxury', 'Luxury'),
        ('Ultra Luxury', 'Ultra Luxury'),
    ]
    OCCUPANCIES = [
        ('Residence', 'Residence'),
        ('Commercial', 'Commercial'),
    ]

    cost_choice = models.CharField(max_length=20, choices=COST_CHOICES,  default='Medium')
    occupancy = models.CharField(max_length=50, choices=OCCUPANCIES,  default='Residence')
    area = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='default/image.png', default='image.png')
    ip_address = models.GenericIPAddressField(default='127.0.0.2')  # Using GenericIPAddressField for IP address
    timestamp = models.DateTimeField(default=timezone.now)  # Removed auto_now_add=True

    class Meta:
        verbose_name_plural = "Costfinder"

    def __str__(self):
        return str(self.area)
