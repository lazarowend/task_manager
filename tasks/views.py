from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm


class ListTask(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'
    queryset = Task.objects.order_by('-status', 'priority')

    
class CreateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'new_task.html'
    success_url = '/tasks/'


class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = '/tasks/'
    context_object_name = 'task'


class DeleteTask(DeleteView):
    model = Task
    template_name = 'home.html'
    success_url = '/tasks/'

