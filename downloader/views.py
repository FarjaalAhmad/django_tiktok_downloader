# from django.conf import settings
from django.shortcuts import render
from . import functions
from django.http import HttpResponse

def home(request):
    return render(request, 'downloader/home.html', {})

def download(request):
    return render(request, 'downloader/download.html', {})

def json(request):
    return HttpResponse("JSON")

def decide(request):
    url = request.POST.get("url")
    todo = int(request.POST.get("todo"))
    if todo == 1:
        return download(request)
    elif todo == 2:
        return json(request)
    else:
        return HttpResponse("Error")
