from . models import ReadRecord
from novel.models import NovelType

# 添加阅读信息
def read_statistics_once_read(request, chapter):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    readRecord = ReadRecord.objects.filter(user_ip=ip, book_id=chapter.book_id).first()
    if readRecord:
        readRecord.chapter_id = chapter.pk
        readRecord.save()
    else:
        ReadRecord.objects.create(user_ip=ip, book_id=chapter.book_id, chapter_id=chapter.pk)

# 获取阅读信息
def get_statistics_info(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    read_history = ReadRecord.objects.filter(user_ip=ip)[:10]
    types = NovelType.objects.all()
    context = {}
    context['types'] = types
    context['read_history'] = read_history
    return context
