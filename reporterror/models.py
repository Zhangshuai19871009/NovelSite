from django.db import models
from django.conf import settings
from novel.models import Novel, Chapter

# 举报小说
class ReportError(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='用户', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', max_length=50)
    content = models.TextField(verbose_name='举报内容')
    report_time = models.DateTimeField(verbose_name='举报时间', auto_now_add=True)

    class Meta():
        ordering = ['-report_time']
