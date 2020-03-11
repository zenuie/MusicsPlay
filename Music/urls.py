from django.urls import path
from Music.views import homepage_view

urlpatterns = [
    path('', homepage_view, name='index')
]
