from django.contrib import admin
from .models import Novel, NovelType, Chapter

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ('id_book', 'book_name', 'author', 'category', 'status', 'image', 'description', 'novel_url', 'update_time')

@admin.register(NovelType)
class NovelTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book', 'chapter_url', 'insert_num')
