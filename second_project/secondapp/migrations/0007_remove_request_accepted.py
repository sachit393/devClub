# Generated by Django 3.2 on 2021-04-16 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0006_request_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='Accepted',
        ),
    ]