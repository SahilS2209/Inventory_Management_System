# Generated by Django 4.0.3 on 2022-10-24 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prod_app', '0002_rename_cate_name_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_name',
            new_name='product_name',
        ),
    ]
