# Generated by Django 3.0.6 on 2020-07-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('section_id', models.CharField(choices=[('0', 'پیش دبستانی'), ('1', 'اول ابتدایی'), ('2', 'دوم ابتدایی'), ('3', 'سوم ابتدایی'), ('4', 'چهارم ابتدایی'), ('5', 'پنجم ابتدایی'), ('6', 'ششم'), ('7', 'هفتم'), ('8', 'هشتم'), ('9', 'نهم'), ('10', 'پرسنل')], default='0', max_length=2)),
            ],
        ),
    ]
