# Generated by Django 5.0.7 on 2024-08-07 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
        ('employees', '0003_employee_is_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attendance',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verified_attendance', to='employees.employee'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='check_out_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]