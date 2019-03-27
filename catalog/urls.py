from django.urls import path

from catalog import views

urlpatterns = [
    # '.../'
    path('', views.index, name='index'),
    # '.../author/slug_author'
    path('author/<slug>/', views.AuthorDetailView.as_view(), name='author'),
    # '.../genre/genre_slug'
    path('genre/<slug>/', views.GenreDetailView.as_view(), name='genre'),
    path('book/<slug>/', views.BookDetailView.as_view(), name='book'),
]