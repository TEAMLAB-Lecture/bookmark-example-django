from django.shortcuts import render
from django.http import HttpResponse

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'hello.html', {'time': now})

def hello(request, user_name):
    spams = ['spam ' + user_name, 'Spam ' + user_name, 'SPAM! ' + user_name]
    return render(request, 'spams.html', {'spams': spams})
