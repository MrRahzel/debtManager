# Generated by Django 3.2.8 on 2022-04-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_products_to_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='to_who',
            field=models.CharField(default='NULL', max_length=200),
        ),
    ]