# Generated by Django 3.0.6 on 2020-07-08 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
        ('ClassActivity', '0002_weeklyschedule'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='weeklyschedule',
            unique_together={('class_id', 'week_day')},
        ),
    ]