# Generated by Django 3.2 on 2021-04-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('author', models.CharField(max_length=264)),
                ('publisher', models.CharField(max_length=264)),
                ('genre', models.CharField(max_length=264)),
                ('summary', models.CharField(max_length=3000)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
