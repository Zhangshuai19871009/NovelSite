import datetime
from django.db import models
from novel.models import Chapter, Novel

# 阅读记录
class ReadRecord(models.Model):
    user_ip = models.CharField(verbose_name='用户IP', max_length=20)
    book = models.ForeignKey(Novel, verbose_name='书编', on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, verbose_name='章节ID', on_delete=models.CASCADE)
    read_time = models.DateTimeField(verbose_name='阅读时间', auto_now=True)

    class Meta():
        verbose_name = '阅读记录'
        verbose_name_plural = verbose_name
        ordering = ['-read_time']
