# Generated by Django 4.1 on 2024-08-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0008_alter_recordssport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordssport',
            name='units',
            field=models.CharField(choices=[('weight', 'Kilogrammes'), ('time', 'Temps'), ('distance_km', 'Distance en Km'), ('distance_m', 'Distance en Mètre'), ('points', 'Points'), ('free', 'Personnalisé')], max_length=20),
        ),
    ]
