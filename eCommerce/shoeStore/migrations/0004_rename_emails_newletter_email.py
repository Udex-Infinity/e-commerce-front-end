# Generated by Django 4.2.4 on 2023-10-30 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoeStore', '0003_newletter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newletter',
            old_name='emails',
            new_name='email',
        ),
    ]
