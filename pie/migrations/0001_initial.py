# Generated by Django 4.2.2 on 2023-08-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piechart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Costfinder',
            },
        ),
    ]
