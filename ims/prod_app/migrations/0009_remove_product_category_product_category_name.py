# Generated by Django 4.0.3 on 2022-10-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_app', '0008_alter_customer_last_name_alter_customer_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]