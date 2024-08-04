# Generated by Django 4.1 on 2024-08-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_recordssportuser_date_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordssport',
            name='general',
            field=models.BooleanField(default=False, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='recordssport',
            name='groups',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
