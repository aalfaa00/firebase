# Generated by Django 4.1.1 on 2022-09-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
    ]
