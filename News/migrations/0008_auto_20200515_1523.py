# Generated by Django 3.0.6 on 2020-05-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_auto_20200514_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]