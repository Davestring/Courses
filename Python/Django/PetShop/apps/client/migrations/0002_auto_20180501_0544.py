# Generated by Django 2.0.2 on 2018-05-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='genre',
        ),
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]