# Generated by Django 4.1 on 2022-11-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_index_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address_zh_hans',
            field=models.CharField(max_length=250, null=True, verbose_name='Адрес проживания'),
        ),
        migrations.AddField(
            model_name='order',
            name='city_zh_hans',
            field=models.CharField(max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name_zh_hans',
            field=models.CharField(max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name_zh_hans',
            field=models.CharField(max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]
