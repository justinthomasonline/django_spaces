# Generated by Django 2.2.13 on 2020-06-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_auto_20200629_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createagency',
            name='PaymentExpiry',
            field=models.DateField(blank=True),
        ),
    ]
