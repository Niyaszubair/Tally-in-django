# Generated by Django 4.0.5 on 2022-08-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_analysis_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis_view',
            name='stgroup',
        ),
    ]
