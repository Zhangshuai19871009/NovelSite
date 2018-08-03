from django.urls import path
from . import views

urlpatterns = [
    path('add_to_bookshelf/', views.add_to_bookshelf, name='add_to_bookshelf'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('get_shelf_list/', views.get_shelf_list, name='get_shelf_list'),
    path('delete_one_book/', views.delete_one_book, name='delete_one_book'),
    path('delete_choice_book/', views.delete_choice_book, name='delete_choice_book'),
]