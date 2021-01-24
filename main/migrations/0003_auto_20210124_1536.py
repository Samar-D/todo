# Generated by Django 3.1.5 on 2021-01-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]