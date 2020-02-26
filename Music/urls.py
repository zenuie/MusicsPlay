from django.urls import path
from .views import Music_list

urlpatterns = [
    path('music/', Music_list),
]
