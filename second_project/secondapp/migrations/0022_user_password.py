# Generated by Django 3.2 on 2021-04-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0021_warnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='library', max_length=200),
        ),
    ]
