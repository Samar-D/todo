# Generated by Django 3.1.5 on 2021-01-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210125_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='year',
            field=models.IntegerField(),
        ),
    ]
