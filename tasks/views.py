from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

import tasks

def index(request):
    return render(request, 'tasks/vhod.html')

def matrix(request):
    return HttpResponse("Матрица Эзенхауэра")
