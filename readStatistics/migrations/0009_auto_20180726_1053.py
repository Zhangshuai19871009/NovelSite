# Generated by Django 2.0.5 on 2018-07-26 02:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('readStatistics', '0008_auto_20180726_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readrecord',
            name='read_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 26, 2, 53, 13, 59326, tzinfo=utc), verbose_name='阅读时间'),
        ),
    ]
