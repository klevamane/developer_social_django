# Generated by Django 2.2 on 2019-04-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0005_auto_20190408_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='mobile',
            field=models.CharField(error_messages={'unique': 'A user already registered with this mobile number'}, max_length=11, unique=True),
        ),
    ]
