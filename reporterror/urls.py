from django.urls import path
from . import views

urlpatterns = [
    path('to_novel_error/', views.to_novel_error, name='to_novel_error'),
    path('report_error_form/<str:book_id>,<int:chapter_id>', views.report_error_form, name='report_error_form'),
    path('delete_report', views.delete_report, name='delete_report'),
    path('get_report_detail/<int:report_id>', views.get_report_detail, name='get_report_detail'),
    path('delete_by_id/<int:report_id>', views.delete_by_id, name='delete_by_id'),
]