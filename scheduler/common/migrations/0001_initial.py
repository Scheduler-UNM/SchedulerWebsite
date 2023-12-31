# Generated by Django 5.0.1 on 2024-01-04 21:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('building', models.CharField(default='unm', max_length=64)),
                ('building_info', models.CharField(default='null', max_length=64)),
                ('pod_supervisor', models.CharField(default='null', max_length=64)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('pod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='common.pod')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('swap', 'Swap'), ('coverage', 'Coverage'), ('giveaway', 'Giveaway')], max_length=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requested_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.shift')),
                ('requesting_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
