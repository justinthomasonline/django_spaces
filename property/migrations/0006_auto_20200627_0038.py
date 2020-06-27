# Generated by Django 2.2.13 on 2020-06-26 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20200627_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='Latitude',
            field=models.DecimalField(decimal_places=6, default=django.utils.timezone.now, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='Longitude',
            field=models.DecimalField(decimal_places=6, default=django.utils.timezone.now, max_digits=9),
            preserve_default=False,
        ),
    ]