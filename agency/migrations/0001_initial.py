# Generated by Django 2.2.13 on 2020-06-20 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AgencyName', models.CharField(max_length=200)),
                ('Logo', models.ImageField(upload_to='AgencyAssets')),
                ('HeadOfficeAddress', models.TextField()),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Email', models.EmailField(max_length=70, unique=True)),
                ('AgencyDescription', models.TextField()),
                ('CRNumber', models.IntegerField()),
                ('SupportingDocument', models.FileField(upload_to='AgencyAssets')),
                ('SupportingDocumentExpiry', models.DateField()),
                ('Active', models.BooleanField(default=False)),
                ('PaymentRequired', models.BooleanField(default=True)),
                ('PaymentExpiry', models.DateField()),
                ('NewRequest', models.BooleanField(default=True)),
                ('Roles', models.CharField(default='agency', max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='AgencyAssets')),
                ('Nationality', models.TextField()),
                ('Languages', models.TextField()),
                ('OfficeAddress', models.TextField()),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Email', models.EmailField(max_length=70, unique=True)),
                ('Description', models.TextField()),
                ('Active', models.BooleanField(default=False)),
                ('Roles', models.CharField(default='agent', max_length=20)),
                ('Agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.CreateAgency')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]