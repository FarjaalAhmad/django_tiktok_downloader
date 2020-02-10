# from django.conf import settings
from django.shortcuts import render
from . import functions
from django.http import HttpResponse
import simplejson


def home(request):
    return render(request, 'downloader/home.html', {})

def download(request,url):
    dict = functions.downloader(url)
    dict = simplejson.loads(dict)
    return render(request, 'downloader/download.html', {"watermark":dict["watermark"],"without_watermark":dict["without_watermark"],"audio":dict["audio"]})

def json(request,url):
    dict = functions.downloader(url)
    return HttpResponse(dict)

def decide(request):
    url = request.POST.get("url")
    todo = int(request.POST.get("todo"))
    if todo == 1:
        return download(request,url)
    elif todo == 2:
        return json(request,url)
    else:
        return HttpResponse("Are Jigar! Tu Idhar Kidhar?")
