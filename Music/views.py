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
class MusicAPIView(APIView):
    def get(self,request):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MusicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicAPIViewDetail(APIView):
    def get_object(self,id):
        try:
            return Music.objects.get(id =id)
        except Music.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        music = self.get_object(id)
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    def put(self,request,id):
        music = self.get_object(id)
        serializer = MusicSerializer(music,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        music = self.get_object(id)
        music.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "youtube.html", {})


@api_view(['GET','POST'])
def Music_list(request):
    if request.method == 'GET':
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Music_detail(request,pk):
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Music.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
