# Generated by Django 4.1 on 2022-11-29 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_category_es_product_category_zh_hans_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_zh_hans',
            new_name='category_ja',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_zh_hans',
            new_name='description_ja',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_zh_hans',
            new_name='name_ja',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='short_description_zh_hans',
            new_name='short_description_ja',
        ),
    ]
