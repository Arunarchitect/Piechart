# Generated by Django 4.2.4 on 2023-08-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0012_alter_costfinder_cost_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='costfinder',
            name='occupancy',
            field=models.CharField(choices=[('Residence', 'Residence'), ('Commercial', 'Commercial')], default='Residence', max_length=50),
        ),
    ]