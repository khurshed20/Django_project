# Generated by Django 3.2.5 on 2022-12-10 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_Api', '0002_company_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='owner',
        ),
    ]