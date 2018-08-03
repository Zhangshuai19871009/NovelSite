from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings
from .models import Novel, Chapter, NovelType
from readStatistics.utils import read_statistics_once_read, get_statistics_info
from bookshelf.models import AddShelfNum
from bookvote.models import VoteTotal

# 小说分页查询
def get_novel_list_common_data(request, novel_list):
    paginator = Paginator(novel_list, settings.EACH_PAGE_BLOGS_NUMBER)# 每页显示条数
    page_num = request.GET.get('page', 1)# 获取url的页码参数（GET请求）
    page_of_novels = paginator.get_page(page_num)
    current_page_num = page_of_novels.number # 获取当前页码
    # 获取当前页的前后两页
    page_range = [i for i in range(max(current_page_num - 2, 1), min(current_page_num + 2, paginator.num_pages) + 1)]
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = get_statistics_info(request)
    # 需要查找的所有小说
    context['novel_list'] = page_of_novels.object_list
    # 分页显示的小说
    context['page_of_novels'] = page_of_novels
    # 分页页码
    context['page_range'] = page_range
    return context

# 根据小说类别查询
def get_novel_of_type(request, novelType_pk):
    novel_list = Novel.objects.filter(category=novelType_pk)
    context = get_novel_list_common_data(request, novel_list)
    novel_type = NovelType.objects.filter(pk=novelType_pk).first()
    context['type'] = novel_type
    return render(request, 'novel/novel_type_list.html', context)


# 根据书名获取小说
def get_novel_by_name(request):
    bookname = request.POST.get('bookname')
    novel_list = Novel.objects.filter(book_name=bookname)
    context = get_novel_list_common_data(request, novel_list)
    context['bookname'] = bookname
    return render(request, 'novel/novel_serach.html', context)

# 获取小说和分类信息
def get_novel_and_novelType(request, novel_pk):
    novel = Novel.objects.filter(pk=novel_pk).first()
    context = get_statistics_info(request)
    context['novel'] = novel
    return context

# 获取小说详细信息
def get_novel_detail(request, novel_pk):
    chapters = Chapter.objects.filter(book_id=novel_pk).order_by('-insert_num')[:7]
    shelfnum = AddShelfNum.objects.filter(book_id=novel_pk).first()
    if shelfnum:
        shelf_num = shelfnum.num
    else:
        shelf_num = 0
    votetotal = VoteTotal.objects.filter(book_id=novel_pk).first()
    if votetotal:
        vote_count = votetotal.vote_count
    else:
        vote_count = 0
    context = get_novel_and_novelType(request, novel_pk)
    context['chapters'] = chapters
    context['shelf_num'] = shelf_num
    context['vote_count'] = vote_count
    return render(request, 'novel/novel_detail.html', context)

# 获取小说章节
def get_chapter_list(request, novel_pk):
    chapter_list = Chapter.objects.filter(book_id=novel_pk).order_by('insert_num')
    context = get_novel_and_novelType(request, novel_pk)
    context['chapter_list'] = chapter_list
    return render(request, 'novel/chapter_list.html', context)

# 获取小说内容
def get_chapter_content(request, insert_num):
    chapter = Chapter.objects.filter(insert_num=insert_num).first()
    read_statistics_once_read(request, chapter)
    chapter_list = Chapter.objects.filter(book_id=chapter.book_id).order_by('insert_num')
    first = chapter_list.first()
    last = chapter_list.last()
    context = get_novel_and_novelType(request, chapter.book_id)
    context['first'] = first
    context['last'] = last
    context['pre'] = chapter.insert_num - 1
    context['next'] = chapter.insert_num + 1
    context['chapter'] = chapter
    return render(request, 'novel/chapter_detail.html', context)
