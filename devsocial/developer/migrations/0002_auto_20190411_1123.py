# Generated by Django 2.2 on 2019-04-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
