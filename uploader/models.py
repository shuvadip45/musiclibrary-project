from django.db import models

# Create your models here.

from django.forms import ModelForm
from django import forms

class Upload(models.Model):
    songfile = models.FileField(upload_to="songs/")
    upload_date = models.DateTimeField(auto_now_add =True)
    albumartist = models.CharField(max_length=30, default='foobar')
    songname = models.CharField(max_length=50, default='foobar')
    artist = models.CharField(max_length=100, default='foobar')
    genre = models.CharField(max_length=20, default='foobar')
    album = models.CharField(max_length=40, default='foobar')
    releaseyear = models.IntegerField(default=0)
    tracknumber = models.IntegerField(default=0)


# FileUpload form class.
class UploadForm(ModelForm):

    class Meta:
        model = Upload
        fields = ('songfile', 'albumartist', 'songname', 'artist', 'genre', 'album', 'releaseyear', 'tracknumber')
