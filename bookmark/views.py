from django.shortcuts import render
from django.http import HttpResponse
from bookmark.models import Bookmark

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'hello.html', {'time': now})

def hello(request, user_name):
    spams = ['spam ' + user_name, 'Spam ' + user_name, 'SPAM! ' + user_name]
    return render(request, 'spams.html', {'spams': spams})

def index(request):
    return render(request, 'index.html', {"project_name": "TeamLab"})

def bookmark(request):
    all_bookmark = None
    if request.method == 'POST':
        bookmark = Bookmark(bookmark_name=request.POST["bookmark_name"], bookmark_url=request.POST["bookmark_url"])
        bookmark.save()
        all_bookmark = Bookmark.objects.all()

        result = {"all_bookmark": all_bookmark,
                  "bookmark_name": request.POST["bookmark_name"],
                  "bookmark_url": request.POST["bookmark_url"]}

        return render(request, 'bookmark.html', result )
    else:
        all_bookmark = Bookmark.objects.all()
        result = {"all_bookmark" : all_bookmark}
        return render(request, 'bookmark.html', result )

def login(request):
    return render(request, 'login_form.html')

def check_login(request):
    if request.method == 'POST':
        print("Hello Login")
        email = request.POST["email"]
        print(email)
        request.session['login_id'] = email
        return render(request, 'index.html', {"login_id": email})
