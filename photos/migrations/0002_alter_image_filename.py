# Generated by Django 3.2 on 2021-09-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='filename',
            field=models.ImageField(height_field=1200, upload_to='images/', width_field=1600),
        ),
    ]
