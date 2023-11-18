# Generated by Django 4.1.7 on 2023-10-27 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0007_alter_institution_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.institution')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.medication_package')),
            ],
        ),
        migrations.CreateModel(
            name='auditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditorID', models.IntegerField()),
                ('auditorName', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]