# Generated by Django 4.1.7 on 2023-10-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_remove_medication_package_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication_package',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]