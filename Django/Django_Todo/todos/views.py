from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def index(request):
  todos = Todo.objects.order_by('priority')
  context = {
    "todos" : todos,
  }

  return render(request, 'todos/index.html', context)

def create(request):
  name = request.GET.get('name')
  content = request.GET.get("content")
  priority = request.GET.get('priority')
  created_at = request.GET.get('created_at')
  deadline = request.GET.get('deadline')
  # print(content)
  Todo.objects.create(
    name=name,
    content=content,
    priority=priority,
    created_at=created_at,
    deadline=deadline,
  )

  return redirect('todos:index')

def change(request,pk):
  target = Todo.objects.get(id = pk)
  if target.completed:
    target.completed = False
  else:
    target.completed = True
  target.save()
  return redirect('todos:index')

def delete(request, pk):
  todo = Todo.objects.get(id = pk)
  todo.delete()
  
  return redirect('todos:index')
