# Generated by Django 4.0.5 on 2022-08-21 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_createstockitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstockitem',
            name='under',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createstockgrp'),
        ),
    ]