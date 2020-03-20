from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Music
from .serializers import MusicSerializer


# Create your views here.
def homepage_view(request, *args, **kwargs):
    return render(request, "index.html")


def songList(request, *args, **kwargs):
    return render(request, "template/song_list.html")


def singerList(request, *args, **kwargs):
    return render(request, "template/singer_list.html")


def Genre(request, *args, **kwargs):
    return render(request, "template/genre.html")


def Contact(request, *args, **kwargs):
    return render(request, "template/contact.html")


def AboutMe(request, *args, **kwargs):
    return render(request, "template/about_me.html")

def Test(request, *args, **kwargs):
    return render(request, "template/test.html")