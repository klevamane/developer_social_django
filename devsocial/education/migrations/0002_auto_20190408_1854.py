# Generated by Django 2.2 on 2019-04-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='to',
            field=models.DateField(blank=True, null=True),
        ),
    ]