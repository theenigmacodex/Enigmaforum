# Generated by Django 3.0.4 on 2020-06-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200609_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentimg',
            field=models.ImageField(default='', upload_to='comment_pics', verbose_name='Post Image'),
        ),
    ]