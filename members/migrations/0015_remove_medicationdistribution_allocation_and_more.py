# Generated by Django 4.1.7 on 2023-11-06 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_medicationdistribution_allocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationdistribution',
            name='allocation',
        ),
        migrations.DeleteModel(
            name='InstitutionAllocation',
        ),
    ]