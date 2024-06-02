from django.shortcuts import render

# Create your views here.
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render


def registry(request):
    context={
        "notes": 'task_list',
    }
    return render(request, 'registry.html', context)
