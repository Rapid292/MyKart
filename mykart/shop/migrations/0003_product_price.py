# Generated by Django 3.0.5 on 2020-04-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200420_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, max_length=50),
        ),
    ]
