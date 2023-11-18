# Generated by Django 4.1.7 on 2023-10-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County_Health_Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerID', models.IntegerField(max_length=255)),
                ('fullName', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_ID', models.IntegerField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
