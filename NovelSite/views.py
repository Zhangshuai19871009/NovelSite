from django.shortcuts import render
from novel.models import Novel
from readStatistics.utils import get_statistics_info

def home(request):
    novels = Novel.objects.all()[:14]
    context = get_statistics_info(request)
    context['novels'] = novels
    return render(request, 'home.html', context)
