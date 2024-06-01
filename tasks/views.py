from asyncio import TaskGroup
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.utils import timezone
from datetime import timedelta

from tasks.models import Task

def index(request):
    task_list=Task.objects.all()
    context={
        "task": task_list,
    }
    return render(request, 'tasks/vhod.html', context)

def matrix(request):
    task_list_1=Task.objects.filter(important=True).filter(urgently=True)
    task_list_2=Task.objects.filter(important=True).filter(urgently=False)
    task_list_3=Task.objects.filter(important=False).filter(urgently=True)
    task_list_4=Task.objects.filter(important=False).filter(urgently=False)
    context={
        "cont1": task_list_1,
        "cont2": task_list_2,
        "cont3": task_list_3,
        "cont4": task_list_4,
    }
    return render(request, 'tasks/matrica.html', context)

def list_week(request):
    current_date = timezone.now().date()

    # Находим день недели для текущей даты (0 - понедельник, 1 - вторник, ..., 6 - воскресенье)
    current_weekday = current_date.weekday()

    # Вычисляем даты для каждого дня недели
    current_date1 = current_date - timedelta(days=current_weekday)  # Понедельник
    current_date2 = current_date1 + timedelta(days=1)  # Вторник
    current_date3 = current_date1 + timedelta(days=2)  # Среда
    current_date4 = current_date1 + timedelta(days=3)  # Четверг
    current_date5 = current_date1 + timedelta(days=4)  # Пятница
    current_date6 = current_date1 + timedelta(days=5)  # Суббота
    current_date7 = current_date1 + timedelta(days=6)  # Воскресенье

    # Фильтруем объекты Task для каждой даты текущей недели
    todos_filtered1 = Task.objects.filter(todo_date=current_date1)
    todos_filtered2 = Task.objects.filter(todo_date=current_date2)
    todos_filtered3 = Task.objects.filter(todo_date=current_date3)
    todos_filtered4 = Task.objects.filter(todo_date=current_date4)
    todos_filtered5 = Task.objects.filter(todo_date=current_date5)
    todos_filtered6 = Task.objects.filter(todo_date=current_date6)
    todos_filtered7 = Task.objects.filter(todo_date=current_date7)

    context={
        "current_date1": current_date1.day,
        "current_date2": current_date2.day,
        "current_date3": current_date3.day,
        "current_date4": current_date4.day,
        "current_date5": current_date5.day,
        "current_date6": current_date6.day,
        "current_date7": current_date7.day,

        "todos_filtered1":todos_filtered1,
        "todos_filtered2":todos_filtered2,
        "todos_filtered3":todos_filtered3,
        "todos_filtered4":todos_filtered4 ,
        "todos_filtered5":todos_filtered5 ,
        "todos_filtered6":todos_filtered6 ,
        "todos_filtered7":todos_filtered7 ,
    }

    return render(request, 'tasks/list_week.html', context)
