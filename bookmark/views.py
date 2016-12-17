from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from bookmark.models import Bookmark

from django.contrib.auth.models import User


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

        return render(request, 'bookmark.html', result)
    else:
        all_bookmark = Bookmark.objects.all()
        result = {"login_id": email,
                  "all_bookmark": all_bookmark}
        return render(request, 'bookmark.html', result)


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
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                request.session['login_id'] = email
                return render(request, 'index.html', {"login_id": email})
            else:
                status = "Password가 틀렸습니다"
                return render(request, 'login_form.html', {"status": status })
        except user.DoesNotExist:
            status = "존재하지 않는 아이디입니다."
            return render(request, 'login_form.html', {"status": status})


def user_registration_process(request):
    if request.method == 'POST':

        email = request.POST["email"]
        try:
            User.objects.get(username=email)
            status = "이미 존재하는 아이디입니다"
            return render(request, 'login_form.html', {"status": status})
        except User.DoesNotExist:
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            password = request.POST["passwd"]
            new_user = User.objects.create_user(email, email, password)
            new_user.last_name = lastname
            new_user.first_name = firstname
            new_user.save()
            request.session['login_id'] = email
            return render(request, 'index.html', {"login_id": email})
