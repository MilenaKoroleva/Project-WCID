from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

import tasks

def index(request):
    return render(request, 'tasks/vhod.html')

def matrix(request):
    return render(request, 'tasks/matrica.html')

def list_week(request):
    return render(request, 'tasks/list_week.html')
