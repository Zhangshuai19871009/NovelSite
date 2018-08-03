# Generated by Django 2.0.5 on 2018-07-23 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novel', '0007_auto_20180720_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(max_length=20, verbose_name='用户IP')),
                ('read_time', models.DateTimeField(auto_now=True, verbose_name='阅读时间')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Novel', verbose_name='书编')),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novel.Chapter', verbose_name='章节ID')),
            ],
            options={
                'verbose_name': '阅读记录',
                'verbose_name_plural': '阅读记录',
                'ordering': ['-read_time'],
            },
        ),
    ]
