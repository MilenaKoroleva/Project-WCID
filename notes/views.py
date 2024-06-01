from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from notes.models import Note

def note(request):
    task_list=Note.objects.all()
    context={
        "notes": task_list,
    }
    return render(request, 'index.html', context)

