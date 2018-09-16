from django.shortcuts import render, redirect
from .models import Todo

def todos(request):
    todo_list = Todo.objects.all().order_by('createdAt').filter(mark=False)
    context = {
        "title": "Tasks in List 1",
        "todos": todo_list,
        "isCompleted": False
    }
    return render(request, 'todo_list.html', context)

def add(request):
    Todo.objects.create(todo=request.POST["task"], dueTo=request.POST["date"], owner="Me").save()
    return redirect('/api/v1/todos/')

def deleteAll(request):
    mark = True if request.POST["isCompleted"] == 'True' else False
    Todo.objects.filter(mark=mark).delete()
    return redirect(path(mark))

def completed(request):
    completed_list = Todo.objects.all().order_by('createdAt').filter(mark=True)
    context = {
        "title": "Completed tasks in List 1",
        "todos": completed_list,
        "isCompleted": True
    }
    return render(request, 'todo_list.html', context)

def markTodo(request, id):
    mark = True if request.POST["isCompleted"] == 'True' else False
    todos = Todo.objects.get(id=id)
    todos.mark = not mark
    todos.save()
    return redirect(path(mark))

def path(mark):
    path = '/api/v1/todos/'
    if mark:
        path += 'completed/'
    return path
