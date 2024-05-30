# Generated by Django 4.1 on 2024-05-29 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_remove_exercise_description'),
        ('users2', '0002_injurie_date_alter_injurie_zone_alter_wellness_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='injurie',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='injurie',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.workzone'),
        ),
        migrations.AlterField(
            model_name='wellness',
            name='date',
            field=models.DateField(),
        ),
    ]