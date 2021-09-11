# Generated by Django 3.2 on 2021-09-11 04:34

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_alter_image_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='filename',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1600, 1200], upload_to='images/'),
        ),
    ]
