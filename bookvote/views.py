import time
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import BookVote, VoteTime, VoteTotal

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

# 投票
def get_book_vote(request):
    user = request.user
    if not user.is_authenticated:
        return ErrorResponse('对不起，您需要登录才能使用本功能！')

    book_id = request.GET.get('book_id')
    votetime = VoteTime.objects.filter(user=user).first()
    if votetime:
        vtime = votetime.vote_time
        ans_vtime = time.mktime(vtime.timetuple())
        dtime = datetime.datetime.now()
        ans_dtime = time.mktime(dtime.timetuple())
        hour = (ans_dtime - ans_vtime)/3600
        if hour < 24:
            return ErrorResponse('对不起，您今天已经用完了推荐的权利！每人每天可以推荐 1 次。')
        else:
            votetime.vote_num += 1
            votetime.save()
            # 投票
            bookvote, created = BookVote.objects.get_or_create(book_id=book_id, user=user)
            bookvote.vote_num += 1
            bookvote.save()
            # 投票总数
            votetotal, created = VoteTotal.objects.get_or_create(book_id=book_id)
            votetotal.vote_count += 1
            votetotal.save()
    else:
        # 投票
        bookvote, created = BookVote.objects.get_or_create(book_id=book_id, user=user)
        bookvote.vote_num += 1
        bookvote.save()
        # 投票总数
        votetotal, created = VoteTotal.objects.get_or_create(book_id=book_id)
        votetotal.vote_count += 1
        votetotal.save()
        # 投票时间
        votetime, created = VoteTime.objects.get_or_create(user=user)
        votetime.vote_num += 1
        votetime.save()
    return SuccessResponse(votetotal.vote_count, '恭喜您，投票成功！')
