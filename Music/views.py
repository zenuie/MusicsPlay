from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Music
from .serializers import MusicSerializer


# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "youtube.html", {})


@csrf_exempt
def Music_list(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MusicSerializer(data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
