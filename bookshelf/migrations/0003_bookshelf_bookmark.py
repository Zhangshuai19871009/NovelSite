# Generated by Django 2.0.5 on 2018-07-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_auto_20180726_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='bookmark',
            field=models.CharField(default=None, max_length=50, verbose_name='书签'),
            preserve_default=False,
        ),
    ]
