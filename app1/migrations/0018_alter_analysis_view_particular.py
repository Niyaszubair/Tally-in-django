# Generated by Django 4.0.5 on 2022-08-22 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_analysis_view_particular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis_view',
            name='particular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createstockgrp'),
        ),
    ]
