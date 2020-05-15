# Generated by Django 3.0.6 on 2020-05-15 17:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20200514_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdoc',
            name='id',
        ),
        migrations.AddField(
            model_name='userdoc',
            name='role',
            field=models.CharField(choices=[('1', 'مدیر'), ('2', 'معاون'), ('3', 'معلم'), ('4', 'دانش آموز')], default='4', max_length=1),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='userProfile',
        ),
    ]
