# Generated by Django 4.1 on 2022-11-29 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_category_en_product_category_es_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_es',
            new_name='category_zh_hans',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_es',
            new_name='description_zh_hans',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_es',
            new_name='name_zh_hans',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='short_description_es',
            new_name='short_description_zh_hans',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_ja',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_ja',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_ja',
        ),
        migrations.RemoveField(
            model_name='product',
            name='short_description_ja',
        ),
    ]
