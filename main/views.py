from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

import main

def settings(request):
    return render(request, 'nastroiki.html')
