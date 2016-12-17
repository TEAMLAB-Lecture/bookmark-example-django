from django.shortcuts import render
from django.http import HttpResponse
from bookmark.models import Bookmark

import datetime


def index(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'index.html')
    return render(request, 'index.html', {"login_id": email})

def bookmark(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'login_form.html')

    all_bookmark = None
    if request.method == 'POST':
        bookmark = Bookmark(bookmark_name=request.POST["bookmark_name"], bookmark_url=request.POST["bookmark_url"])
        bookmark.save()
        all_bookmark = Bookmark.objects.all()

        result = {"login_id": email,
                    "all_bookmark": all_bookmark,
                  "bookmark_name": request.POST["bookmark_name"],
                  "bookmark_url": request.POST["bookmark_url"]}

        return render(request, 'bookmark.html', result )
    else:
        all_bookmark = Bookmark.objects.all()
        result = {"login_id": email,
            "all_bookmark" : all_bookmark}
        return render(request, 'bookmark.html', result )

def login(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'login_form.html')
    return render(request, 'login_form.html', {"login_id": email})

def logout(request):
    try:
        email = request.session['login_id']
    except KeyError as e:
        return render(request, 'login_form.html')
    return render(request, 'logout_form.html', {"login_id": email})

def logout_process(request):
    del request.session['login_id']
    return render(request, 'index.html')

def check_login(request):
    if request.method == 'POST':
        print("Hello Login")
        email = request.POST["email"]
        request.session['login_id'] = email
        return render(request, 'index.html', {"login_id": email})
