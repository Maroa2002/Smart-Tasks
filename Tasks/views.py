from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Tasks
from .forms import TasksForm

# Create your views here.
class TasksListView(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'tasks/tasks_list.html'

class TasksCreateView(CreateView):
    model = Tasks
    form_class = TasksForm
    template_name = 'tasks/tasks_create.html'
    success_url = '/smart/tasks'

class TasksDetailView(DetailView):
    model = Tasks
    template_name ='tasks/tasks_details.html'
    context_object_name = 'task'

class TasksUpdateView(UpdateView):
    model = Tasks
    form_class = TasksForm
    template_name = 'tasks/tasks_create.html'
    success_url = '/smart/tasks'

class TasksDeleteView(DeleteView):
    model = Tasks
    template_name = 'tasks/tasks_delete.html'
    success_url = '/smart/tasks'