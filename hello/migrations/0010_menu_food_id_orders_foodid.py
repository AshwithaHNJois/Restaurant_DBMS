# Generated by Django 4.0.1 on 2022-02-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_orders_foodname'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='food_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='foodid',
            field=models.CharField(default='', max_length=500),
        ),
    ]