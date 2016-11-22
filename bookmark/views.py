from django.shortcuts import render
from django.http import HttpResponse

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hello(request, user_name):
    html = "<html><body>Hello %s.</body></html>" % user_name
    return HttpResponse(html)