# Generated by Django 4.0.3 on 2022-05-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.DateTimeField(blank=True, null=True, verbose_name='оплачен'),
        ),
    ]