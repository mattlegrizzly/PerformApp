# Generated by Django 4.1 on 2024-08-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_alter_workout_date_alter_workout_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_description',
            field=models.TextField(),
        ),
    ]
