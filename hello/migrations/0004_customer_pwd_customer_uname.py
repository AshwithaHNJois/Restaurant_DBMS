# Generated by Django 4.0.1 on 2022-02-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_alter_customer_name_alter_menu_food_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pwd',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AddField(
            model_name='customer',
            name='uname',
            field=models.CharField(default='', max_length=12),
        ),
    ]