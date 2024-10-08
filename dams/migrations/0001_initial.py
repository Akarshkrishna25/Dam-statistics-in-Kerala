# Generated by Django 5.1 on 2024-08-15 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DamStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rainfall', models.DecimalField(decimal_places=2, max_digits=5)),
                ('inflow', models.DecimalField(decimal_places=2, max_digits=10)),
                ('powerhouse_discharge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spillway_release', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dams.dam')),
            ],
            options={
                'unique_together': {('dam', 'date')},
            },
        ),
    ]
