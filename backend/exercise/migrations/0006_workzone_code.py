# Generated by Django 4.1 on 2024-05-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_remove_material_description_exercise_materials_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workzone',
            name='code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]