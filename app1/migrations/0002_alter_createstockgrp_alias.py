# Generated by Django 4.0.5 on 2022-08-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createstockgrp',
            name='alias',
            field=models.CharField(max_length=100, null=True),
        ),
    ]