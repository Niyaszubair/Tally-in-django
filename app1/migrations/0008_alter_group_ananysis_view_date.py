# Generated by Django 4.0.5 on 2022-08-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_group_ananysis_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_ananysis_view',
            name='date',
            field=models.DateField(),
        ),
    ]