# Generated by Django 3.0.4 on 2020-06-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200609_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='I really need to change my bio'),
        ),
    ]
