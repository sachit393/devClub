# Generated by Django 3.2 on 2021-04-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0017_auto_20210418_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='start',
            new_name='stars',
        ),
        migrations.AlterField(
            model_name='ratings',
            name='comments',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
