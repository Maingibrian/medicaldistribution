# Generated by Django 4.1.7 on 2023-09-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
