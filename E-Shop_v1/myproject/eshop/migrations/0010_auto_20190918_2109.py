# Generated by Django 2.2.5 on 2019-09-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0009_auto_20190918_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('m', 'M'), ('fs', 'FS'), ('l', 'L'), ('s', 'S'), ('xl', 'XL')], max_length=100),
        ),
    ]
