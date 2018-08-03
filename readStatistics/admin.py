from django.contrib import admin
from .models import ReadRecord

# Register your models here.
@admin.register(ReadRecord)
class ReadRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_ip', 'book', 'chapter', 'read_time')