# Generated by Django 3.0.6 on 2020-05-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200525_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hey, I am new to Ace Students'),
        ),
    ]
