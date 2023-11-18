# Generated by Django 4.1.7 on 2023-10-23 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='notification',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.medication_package'),
        ),
    ]
