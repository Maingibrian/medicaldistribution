# Generated by Django 4.1.7 on 2023-10-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county_health_worker',
            name='workerID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='institution',
            name='institution_ID',
            field=models.IntegerField(),
        ),
    ]