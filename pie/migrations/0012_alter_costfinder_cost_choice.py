# Generated by Django 4.2.4 on 2023-08-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0011_costfinder_cost_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costfinder',
            name='cost_choice',
            field=models.CharField(choices=[('Ultra Low Cost', 'Ultra Low Cost'), ('Low Cost', 'Low Cost'), ('Medium', 'Medium'), ('Luxury', 'Luxury'), ('Ultra Luxury', 'Ultra Luxury')], default='Medium', max_length=20),
        ),
    ]
