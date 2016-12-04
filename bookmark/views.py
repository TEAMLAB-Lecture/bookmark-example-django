from django.shortcuts import render
from django.http import HttpResponse

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'hello.html', {'time': now})

def hello(request, user_name):
    spams = ['spam ' + user_name, 'Spam ' + user_name, 'SPAM! ' + user_name]
    return render(request, 'spams.html', {'spams': spams})

def index(request):
    return render(request, 'index.html')

def bookmark(request):
    print("Hello")
    return render(request, 'bookmark.html')

def bookmark_create(request):
    print("Create Hello")
    bookmark_dict = {}
    if request.method == 'POST':
        bookmark_dict = {"bookmark_name": request.POST["bookmark_name"], "bookmark_url": request.POST["bookmark_url"]}
        return render(request, 'bookmark.html', bookmark_dict)

    else:
        return render(request, 'bookmark.html', bookmark_dict)