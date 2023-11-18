# Generated by Django 4.1.7 on 2023-11-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_alter_medication_package_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.institution')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.medication_package')),
            ],
        ),
    ]
