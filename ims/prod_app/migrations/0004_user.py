# Generated by Django 4.0.3 on 2022-10-24 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_app', '0003_rename_prod_name_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
