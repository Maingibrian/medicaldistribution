# Generated by Django 4.1.7 on 2023-10-27 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_medicationdistribution_auditor'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationdistribution',
            name='county_Health_Worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.county_health_worker'),
        ),
    ]
