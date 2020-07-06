# Generated by Django 3.0.6 on 2020-07-06 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True, unique=True)),
                ('content', models.CharField(max_length=5000, null=True)),
                ('pic', models.CharField(blank=True, max_length=250, null=True)),
                ('release_date', models.CharField(max_length=50, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('id', 'title')},
            },
        ),
    ]
