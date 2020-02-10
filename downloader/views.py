from django.shortcuts import render
from . import functions

def home(request):

    return render(request, 'downloader/home.html', {})
