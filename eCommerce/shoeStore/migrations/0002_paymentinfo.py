# Generated by Django 4.2.4 on 2023-10-29 19:45

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shoeStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('card_number', models.CharField(max_length=400)),
                ('month', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('date', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
