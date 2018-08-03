from django.db import models

# 小说类型
class NovelType(models.Model):
    name = models.CharField(verbose_name='类型名称', max_length=10)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = '小说类型'
        verbose_name_plural = verbose_name


# 小说信息
class Novel(models.Model):
    id_book = models.CharField(verbose_name='书编', max_length=20, primary_key=True)
    book_name = models.CharField(verbose_name='书名', max_length=20)
    author = models.CharField(verbose_name='作者', max_length=20)
    category = models.ForeignKey(NovelType, verbose_name='类型', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='状态', max_length=20)
    image = models.CharField(verbose_name='封面图片', max_length=100)
    description = models.CharField(verbose_name='描述', max_length=500)
    novel_url = models.CharField(verbose_name='链接源', max_length=100)
    update_time = models.CharField(verbose_name='修改时间', max_length=20)

    def __str__(self):
        return self.book_name

    class Meta():
        verbose_name = '小说'
        verbose_name_plural = verbose_name

# 章节信息
class Chapter(models.Model):
    title = models.CharField(verbose_name='章节标题', max_length=20)
    book = models.ForeignKey(Novel, verbose_name='书编', on_delete=models.CASCADE)
    chapter_url = models.CharField(verbose_name='章节源', max_length=100)
    content = models.TextField(verbose_name='内容')
    insert_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = '章节'
        verbose_name_plural = verbose_name
