from django.shortcuts import render, reverse
from django.http import JsonResponse
from .models import ReportError
from novel.models import Chapter
from .forms import ReportErrorForm
from novel.models import NovelType
from readStatistics.utils import get_statistics_info

# 返回错误信息
def MessageResponse(code, message):
    data = {}
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)

# 小说分类
def get_novel_type(request):
    novel_types = NovelType.objects.all()
    context = get_statistics_info(request)
    context['types'] = novel_types
    return context

# 举报小说
def to_novel_error(request):
    user = request.user
    if not user.is_authenticated:
        return MessageResponse(4001, '对不起，您需要登录才能使用本功能！')
    if ReportError.objects.all().count() >= 50:
        return MessageResponse(4002, '您的举报条数已满，举报信息最多50条！')
    return MessageResponse(4000, '举报成功')

# 举报表单
def report_error_form(request, book_id, chapter_id):
    user = request.user
    context = get_novel_type(request)
    if request.method == 'POST':
        report_form = ReportErrorForm(request.POST, user)
        if report_form.is_valid():
            title = report_form.cleaned_data['title']
            content = report_form.cleaned_data['content']
            novle_error = ReportError.objects.create(user=user, title=title, content=content)
            novle_error.save()
            report_list = ReportError.objects.all()
            context['report_list'] = report_list
            context['message'] = '举报成功'
            return render(request, 'report/report_message.html', context)
    else:
        if chapter_id == 0:
            report_form = ReportErrorForm(initial={'title': '举报违禁小说！！！', 'content': '小说ID(' + book_id + ')：'})
        else:
            chapter = Chapter.objects.filter(pk=chapter_id).first()
            title = chapter.book.book_name + '--章节错误'
            content = '错误章节：章节目录 ' + chapter.title + '举报原因如下：'
            report_form = ReportErrorForm(initial={'title': title, 'content': content})

    context['report_form'] = report_form
    return render(request, 'report/reporterror.html', context)

# 删除举报
def delete_report(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('check_box_list')
        for id in id_list:
            ReportError.objects.filter(pk=id).delete()
    else:
        if request.GET.get('id') == 'delall':
            ReportError.objects.all().delete()

    report_list = ReportError.objects.all()
    context = get_novel_type(request)
    context['report_list'] = report_list
    return render(request, 'report/report_list.html', context)

# 举报详情
def get_report_detail(request, report_id):
    report = ReportError.objects.filter(pk=report_id).first()
    context = get_novel_type(request)
    context['report'] = report
    return render(request, 'report/report_detail.html', context)

# 根据id删除
def delete_by_id(request, report_id):
    ReportError.objects.filter(pk=report_id).delete()
    context = get_novel_type(request)
    context['message'] = '删除成功'
    return render(request, 'report/report_message.html', context)

