# Generated by Django 3.1.5 on 2021-01-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210124_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
