from django.urls import path
from . import views

urlpatterns = [
    path('get_book_vote/', views.get_book_vote, name='get_book_vote'),
]