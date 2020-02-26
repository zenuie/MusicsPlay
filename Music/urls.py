from django.urls import path
from .views import Music_list,Music_detail,MusicAPIView,MusicAPIViewDetail

urlpatterns = [
    path('MusicAPIView/',MusicAPIView.as_view()),
    path('detail/<int:pk>', MusicAPIViewDetail.as_view()),
]
