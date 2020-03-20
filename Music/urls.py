from django.urls import path
from Music import views

urlpatterns = [
    path('index/', views.homepage_view, name='index'),
    path('song_list/', views.songList, name='song_list'),
    path('singer_list/', views.singerList, name='singer_list'),
    path('genre/', views.Genre, name='genre'),
    path('contact/', views.Contact, name='contact'),
    path('about_me/', views.AboutMe, name='about_me'),
    path('test/', views.Test, name='test'),
]
