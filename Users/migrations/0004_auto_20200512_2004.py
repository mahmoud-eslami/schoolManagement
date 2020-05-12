# Generated by Django 3.0.6 on 2020-05-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20200512_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.AddField(
            model_name='userdoc',
            name='gender',
            field=models.CharField(choices=[('1', 'آقا'), ('0', 'خانوم')], default='1', max_length=4),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='section',
            field=models.CharField(choices=[('0', 'پیش دبستانی'), ('1', 'اول ابتدایی'), ('2', 'دوم ابتدایی'), ('3', 'سوم ابتدایی'), ('4', 'چهارم ابتدایی'), ('5', 'پنجم ابتدایی')], default='0', max_length=4),
        ),
    ]
