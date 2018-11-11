from django.shortcuts import render

# Create your views here.
import os
from uploader.models import UploadForm,Upload
from django.http import HttpResponseRedirect
from django.urls import reverse
import eyed3

def home(request):
    if request.method=="POST":
        song = UploadForm(request.POST, request.FILES)
        if song.is_valid():
            song.save()
            objs=Upload.objects.all()
            obj=objs[len(objs)-1]
            filename=obj.songfile.name
            if filename[-4:]!=".mp3":
                flag=0
                message = "This file is not .mp3"
                id=obj.id
                Upload.objects.filter(id=id).delete()
                return render(request,'upload.html',{'message':message,'flag':flag})
            else:

                audiofile = eyed3.load(os.getcwd()+obj.songfile.url)
                audiofile.tag.artist = obj.artist
                audiofile.tag.album = obj.album
                audiofile.tag.title = obj.songname
                audiofile.tag.album_artist = obj.albumartist
                audiofile.tag.track = obj.tracknumber
                audiofile.tag.save()
                return HttpResponseRedirect(reverse('songupload'))
    else:
        song=UploadForm()
        flag=1
        message=""
    songs=Upload.objects.all().order_by('-upload_date')
    return render(request,'upload.html',{'form':song,'songs':songs,'message':message,'flag':flag})
