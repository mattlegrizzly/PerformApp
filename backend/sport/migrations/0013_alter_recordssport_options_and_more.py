# Generated by Django 4.1 on 2024-08-04 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0012_alter_recordssport_options_recordssport_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordssport',
            options={'ordering': ['groups__is_general', 'order']},
        ),
        migrations.AddField(
            model_name='recordsgroupsport',
            name='is_general',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recordsgroupsport',
            name='sport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='group_sports', to='sport.sport'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recordsgroupsport',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recordssport',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sport.recordsgroupsport'),
        ),
        migrations.AlterUniqueTogether(
            name='recordsgroupsport',
            unique_together={('name', 'sport')},
        ),
    ]