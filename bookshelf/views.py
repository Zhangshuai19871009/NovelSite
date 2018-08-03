from django.shortcuts import render
from django.http import JsonResponse
from .models import Bookshelf, AddShelfNum, BookshelfGroup
from readStatistics.utils import get_statistics_info

# 返回错误信息
def ErrorResponse(message):
    data = {}
    data['status'] = 'ERROR'
    data['message'] = message
    return JsonResponse(data)

# 返回成功数据
def SuccessResponse(num, message):
    data = {}
    data['status'] = 'SUCCESS'
    data['num'] = num
    data['message'] = message
    return JsonResponse(data)

# 添加图书到书架
def add_to_bookshelf(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse('对不起，您需要登录才能使用本功能！')

    if Bookshelf.objects.filter(user=user).count() >= 66:
        return ErrorResponse('对不起，您的书架已满，不能继续添加！')

    book_id = request.GET.get('book_id')

    if Bookshelf.objects.filter(book_id=book_id, user=user).exists():
        return ErrorResponse('sorry，此书已加入书架，不能重复加入！')
    else:
        bookshelf = Bookshelf.objects.create(book_id=book_id, user=user)
        bookshelf.shelfgroup_id = 1
        bookshelf.save()
        shelfnum, created = AddShelfNum.objects.get_or_create(book_id=book_id)
        shelfnum.num += 1
        shelfnum.save()
        return SuccessResponse(shelfnum.num, '恭喜您，此书已成功加入书架！')

# 添加书签
def add_bookmark(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse('对不起，您需要登录才能使用本功能！')

    book_id = request.GET.get('book_id')
    chapter_id = request.GET.get('chapter_id')
    if Bookshelf.objects.filter(book_id=book_id, user=user).exists():
        book_shelf = Bookshelf.objects.filter(book_id=book_id, user=user).first()
        book_shelf.bookmark_id = chapter_id
        book_shelf.shelfgroup_id = 1
        book_shelf.save()
    else:
        # 添加书签
        bookshelf, created = Bookshelf.objects.get_or_create(book_id=book_id, user=user)
        bookshelf.bookmark_id = chapter_id
        bookshelf.save()
        # 加入书架
        shelfnum, created = AddShelfNum.objects.get_or_create(book_id=book_id)
        shelfnum.num += 1
        shelfnum.save()
    return SuccessResponse(-1, '恭喜您，书签添加成功！')

# 书架列表页
def get_shelf_list(request):
    group_id = int(request.GET.get('group_id'))
    context = get_novel_type(request, group_id)
    return render(request, 'shelf/bookshelf_list.html', context)

# 小说分类
def get_novel_type(request, group_id):
    book_list = Bookshelf.objects.all()
    group_list = BookshelfGroup.objects.all()
    group_book_list = Bookshelf.objects.filter(shelfgroup_id=group_id)
    context = get_statistics_info(request)
    context['book_list'] = book_list
    context['group_book_list'] = group_book_list
    context['group_list'] = group_list
    context['select'] = group_id
    return context

# 删除一本书
def delete_one_book(request):
    shelf_id = int(request.GET.get('shelf_id'))
    group_id = int(request.GET.get('group_id'))
    Bookshelf.objects.filter(pk=shelf_id).delete()
    context = get_novel_type(request, group_id)
    return render(request, 'shelf/bookshelf_list.html', context)

# 删除/修改选中的图书
def delete_choice_book(request):
    id_list = request.POST.getlist('check_box_list')
    shelfgroup_id = int(request.POST.get('shelfgroup_id'))
    group_id = int(request.POST.get('group_id'))
    for id in id_list:
        if shelfgroup_id == 0:
            Bookshelf.objects.filter(pk=id).delete()
        else:
            print(111)
            bookshelf = Bookshelf.objects.filter(pk=id).first()
            bookshelf.shelfgroup_id = shelfgroup_id
            bookshelf.save()

    context = get_novel_type(request, group_id)
    return render(request, 'shelf/bookshelf_list.html', context)
