from django.urls import path
from . import views

urlpatterns = [
    path('<int:novelType_pk>', views.get_novel_of_type, name='get_novel_of_type'),
    path('get_novel_detail/<str:novel_pk>', views.get_novel_detail, name='get_novel_detail'),
    path('get_chapter_list/<str:novel_pk>', views.get_chapter_list, name='get_chapter_list'),
    path('get_chapter_content/<int:insert_num>', views.get_chapter_content, name='get_chapter_content'),
    path('get_novel_by_name/', views.get_novel_by_name, name='get_novel_by_name'),
]