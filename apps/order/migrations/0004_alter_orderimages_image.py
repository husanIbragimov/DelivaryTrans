# Generated by Django 4.1.2 on 2022-11-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_transaction_id_alter_order_car_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='OrderImages/'),
        ),
    ]
