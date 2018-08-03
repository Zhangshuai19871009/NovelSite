import datetime
from django.db import models
from django.conf import settings
from novel.models import Novel, Chapter

# 书架组
class BookshelfGroup(models.Model):
    group_name = models.CharField(verbose_name='组名', max_length=20)

    def __str__(self):
        return self.group_name

    class Meta():
        verbose_name = '书架组'
        verbose_name_plural = verbose_name

# 书架
class Bookshelf(models.Model):
    book = models.ForeignKey(Novel, verbose_name='书编', on_delete=models.CASCADE)
    bookmark = models.ForeignKey(Chapter, verbose_name='书签', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    shelfgroup = models.ForeignKey(BookshelfGroup, verbose_name='分组', on_delete=models.CASCADE)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta():
        verbose_name = '书架'
        verbose_name_plural = verbose_name

# 图书加入书架的数量
class AddShelfNum(models.Model):
    book = models.ForeignKey(Novel, verbose_name='书编', on_delete=models.CASCADE)
    num = models.IntegerField(verbose_name='加入书架数量', default=0)

    class Meta():
        verbose_name = '加入书架数量'
        verbose_name_plural = verbose_name
