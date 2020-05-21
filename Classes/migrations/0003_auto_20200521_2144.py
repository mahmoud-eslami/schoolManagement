# Generated by Django 3.0.6 on 2020-05-21 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Classes', '0002_auto_20200521_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userclass',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userclass',
            name='userClass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classes.Classes'),
        ),
    ]