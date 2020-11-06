from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tweet
import cgi
import os
import sys
from datetime import datetime
# Create your views here.

def tweet(request):
    return render(request, 'index.html')

def posttweet(request):
    parent_tweet_id = request.GET.get(key="parent_tweet_id", default=None)
    p_id = {
        'parent_tweet_id': parent_tweet_id,
    }
    return render(request, 'pages/post-tweet.html', p_id)

def home(request):
    database = Tweet.objects.all()
    val = Tweet.objects.values('parent_tweet_id','id','name','text','created_at','image_path')
    mytweet = {
        'db': database,
        'val': val,
    }
    return render(request, 'pages/home.html', mytweet)

def detail(request):
    parent_id = request.GET.get(key="id")
    parent_tweet_id = int(parent_id)
    database = Tweet.objects.all()
    val = Tweet.objects.values(
        'parent_tweet_id','id', 'name', 'text', 'created_at', 'image_path')
    p_id = {
        'parent_tweet_id': parent_tweet_id,
        'val': val,
        'db': database,
    }
    return render(request, 'pages/detail.html',p_id)


def process_form(request):
    fileitem = request.FILES.get('tweet-image', None)
    
    title = request.POST['name']
    comment = request.POST['text']
    dateTime = datetime.now()
    formtype = request.POST['formtype'] 
    parent_tweet_id = request.POST.get('parent_tweet_id', None) or None
    
    if title.strip() == '' or comment.strip() == '' :
        return render(request, 'pages/error.html')
    
    #Test if the file was uploaded
    
    if fileitem:
        #strip leading path from file name to avoid 
        #directory traversal attacks
        
        with open ('tweet/static/tweets/userimage/' + str(fileitem), 'wb+') as destination:
            for chunk in fileitem.chunks():
                destination.write(chunk)
        imageurl = 'tweets/userimage/' + str(fileitem)
    else:
        imageurl = None
        usrmsg = 'No file was uploaded'
        
    new_tweet = Tweet(parent_tweet_id = parent_tweet_id, name = title, text = comment, image_path=imageurl, created_at=dateTime)
    
    new_tweet.save()
    return HttpResponseRedirect(reverse('home'))
