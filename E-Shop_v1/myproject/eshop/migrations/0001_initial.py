# Generated by Django 2.2.5 on 2019-09-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='picture/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('fabric_origin', models.CharField(max_length=100)),
                ('made_in', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('l', 'L'), ('s', 'S'), ('xl', 'XL'), ('fs', 'FS'), ('m', 'M')], max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]