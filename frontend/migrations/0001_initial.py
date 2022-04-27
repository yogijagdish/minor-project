# Generated by Django 4.0.2 on 2022-04-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='climate',
            fields=[
                ('weather', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=255)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=6, primary_key=True, serialize=False)),
                ('temp_min', models.DecimalField(decimal_places=2, max_digits=6)),
                ('temp_max', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
