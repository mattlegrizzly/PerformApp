# Generated by Django 4.1 on 2024-05-29 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='description',
        ),
    ]
