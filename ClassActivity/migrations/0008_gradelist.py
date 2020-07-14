# Generated by Django 3.0.6 on 2020-07-13 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ClassActivity', '0007_auto_20200711_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade_type', models.CharField(choices=[('0', 'امتحان کلاسی'), ('1', 'میانترم'), ('2', 'پایان ترم')], max_length=2)),
                ('grade_count', models.CharField(choices=[('0', 'نیاز به تلاش بیشتر'), ('1', 'قابل قبول'), ('2', 'خوب'), ('3', 'خیلی خوب')], max_length=2)),
                ('day', models.CharField(max_length=5)),
                ('month', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=5)),
                ('grade_owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grade_owner', to=settings.AUTH_USER_MODEL)),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClassActivity.Lessons')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
