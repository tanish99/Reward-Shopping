# Generated by Django 3.0.6 on 2021-04-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='reward_balance',
            field=models.IntegerField(default=0),
        ),
    ]
