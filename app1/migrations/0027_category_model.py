# Generated by Django 4.0.5 on 2022-08-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_sale_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('qnt', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('saleprice', models.IntegerField()),
            ],
        ),
    ]