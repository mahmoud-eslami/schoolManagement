# Generated by Django 3.0.6 on 2020-07-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassActivity', '0006_auto_20200711_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
