# Generated by Django 4.1 on 2024-08-02 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0009_alter_recordssport_units'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recordssportuser',
            old_name='weight_value',
            new_name='record_value',
        ),
    ]