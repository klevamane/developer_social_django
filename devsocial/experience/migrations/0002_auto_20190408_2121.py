# Generated by Django 2.2 on 2019-04-08 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
