# Generated by Django 2.0.5 on 2018-07-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0004_auto_20180712_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='insert_num',
            field=models.IntegerField(default=0),
        ),
    ]
