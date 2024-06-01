from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

import notes

def note(request):
    return render(request, 'index.html')

