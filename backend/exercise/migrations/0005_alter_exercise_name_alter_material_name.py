# Generated by Django 4.1 on 2024-06-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_exercise_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
