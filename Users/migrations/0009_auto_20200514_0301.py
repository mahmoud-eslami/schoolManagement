# Generated by Django 3.0.6 on 2020-05-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20200514_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdoc',
            name='father_jobAddress',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='father_job_pNum',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='home_pNum',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='mother_jobAddress',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='mother_job_pNum',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='mother_nationalCode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='mother_pNum',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userdoc',
            name='user_pNum',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userdoc',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]