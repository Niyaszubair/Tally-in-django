# Generated by Django 4.0.5 on 2022-08-24 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_godown_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase_sale_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('particular', models.CharField(max_length=255)),
                ('qnt', models.IntegerField()),
                ('brate', models.IntegerField()),
                ('bvalue', models.IntegerField()),
                ('addcost', models.IntegerField()),
                ('totalvalue', models.IntegerField()),
                ('itm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.createstockitem')),
            ],
        ),
    ]
