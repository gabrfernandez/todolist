from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todo

# Create your views here.
def home(request):
    todo_items=Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', {"todo_items":todo_items})

def add_todo(request):
    current_date=timezone.now()
    content=request.POST["content"]
    created_obj=Todo.objects.create(text=content, added_date=current_date)
    return redirect( '/')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')