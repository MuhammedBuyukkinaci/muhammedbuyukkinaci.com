# Generated by Django 3.2 on 2021-05-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_order',
            field=models.IntegerField(default=1),
        ),
    ]