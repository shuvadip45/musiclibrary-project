from django.http import HttpResponse
from django.shortcuts import render
import operator
import eyed3

def home(request):
    return render(request,'home.html')

def uploadsong(request):
    return render(request,'uploadsong.html')

def upload(request):
    if request.method=="POST":

        return render(request,'home.html',{'filename':request.FILES['song'].name},{'length':len(request.FILES)})
