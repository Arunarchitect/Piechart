# Generated by Django 4.2.2 on 2023-08-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0005_alter_costfinder_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='costfinder',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='costfinder_images/'),
        ),
    ]
