# Generated by Django 4.1 on 2024-08-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users2', '0008_wellness_nutrition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
