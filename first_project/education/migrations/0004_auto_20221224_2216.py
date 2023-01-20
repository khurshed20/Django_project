# Generated by Django 3.2.5 on 2022-12-24 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_auto_20221224_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordmodel',
            name='views',
        ),
        migrations.AddField(
            model_name='recordmodel',
            name='views',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
