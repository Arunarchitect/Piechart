# Generated by Django 4.2.2 on 2023-08-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0009_alter_costfinder_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costfinder',
            name='image',
            field=models.ImageField(default='image.png', upload_to='default/image.png'),
        ),
    ]
