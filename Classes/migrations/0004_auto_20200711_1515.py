# Generated by Django 3.0.6 on 2020-07-11 15:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Classes', '0003_auto_20200709_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userclass',
            old_name='userClass',
            new_name='class_id',
        ),
        migrations.AlterUniqueTogether(
            name='userclass',
            unique_together={('user', 'class_id')},
        ),
    ]
