from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<str:slug>', views.BookDetailView.as_view(), name='book-detail'),
    # re_path(r'^book/(?P<stub>[-\w]+)$', views.BookDetailView.as_view(), name='book-detail'),


]
