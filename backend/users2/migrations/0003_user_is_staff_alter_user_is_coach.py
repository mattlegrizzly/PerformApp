# Generated by Django 4.1 on 2024-04-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users2', '0002_user_is_active_user_is_coach_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_coach',
            field=models.BooleanField(default=False),
        ),
    ]