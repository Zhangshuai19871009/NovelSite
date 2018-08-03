from django import template
from novel.models import Chapter

register = template.Library()

@register.simple_tag
def get_last_chapter(book_id):
    chapter = Chapter.objects.filter(book_id=book_id).order_by('-insert_num').first()
    return chapter