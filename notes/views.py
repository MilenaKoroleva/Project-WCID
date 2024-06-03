from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from notes.models import Note
from .serializers import NoteSerializer


def note(request):
    task_list=Note.objects.all()
    context={
        "notes": task_list,
    }
    return render(request, 'index.html', context)


@api_view(["POST"])
def save_note(request):
    titel = request.data.get("titel")
    description = request.data.get("description")
    note = Note.objects.create(titel=titel, description=description)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
  