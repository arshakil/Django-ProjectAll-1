# Generated by Django 2.2.5 on 2019-09-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_auto_20190918_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('xl', 'XL'), ('l', 'L'), ('fs', 'FS'), ('s', 'S'), ('m', 'M')], max_length=100),
        ),
    ]