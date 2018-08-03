from django.db import models
from django.conf import settings
from novel.models import Novel

# 投票信息
class BookVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    book = models.ForeignKey(Novel, verbose_name='书编', on_delete=models.CASCADE)
    vote_num = models.IntegerField(verbose_name='投票数', default=0)
    create_time = models.DateTimeField(verbose_name='投票时间', auto_now=True)

    class Meta():
        verbose_name = '投票信息'
        verbose_name_plural = verbose_name

# 投票倒计时
class VoteTime(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    vote_num = models.IntegerField(verbose_name='投票总数', default=0)
    vote_time = models.DateTimeField(verbose_name='投票时间', auto_now=True)

    class Meta():
        verbose_name = '投票时间'
        verbose_name_plural = verbose_name

# 投票总数
class VoteTotal(models.Model):
    book = models.ForeignKey(Novel, verbose_name='书编', on_delete=models.CASCADE)
    vote_count = models.IntegerField(verbose_name='投票总数', default=0)

    class Meta():
        verbose_name = '投票总数'
        verbose_name_plural = verbose_name
