# Generated by Django 4.0.3 on 2022-03-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryApp', '0003_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_items',
            name='item_available_count',
            field=models.IntegerField(default=0),
        ),
    ]
