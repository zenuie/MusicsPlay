from django.db import models


# Create your models here.
class Music(models.Model):
    singer = models.CharField("歌手", max_length=100)
    album = models.CharField("專輯", max_length=100)
    release = models.DateField("專輯發行年分", default="")
    hashtag = models.DecimalField("順序", max_digits=10, decimal_places=0)
    song = models.CharField("歌名", max_length=100)
    lyrics = models.TextField("歌詞", default="可不填")
