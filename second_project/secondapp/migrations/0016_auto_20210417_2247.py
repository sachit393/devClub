# Generated by Django 3.2 on 2021-04-17 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0015_request_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybooks',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.user'),
        ),
        migrations.AlterField(
            model_name='renewalrequests',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.book'),
        ),
        migrations.AlterField(
            model_name='renewalrequests',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.user'),
        ),
    ]