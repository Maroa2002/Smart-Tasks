from django.urls import path

from . import views

urlpatterns = [
    path('tasks', views.TasksListView.as_view(), name='tasks.list'),
    path('tasks/new', views.TasksCreateView.as_view(), name='tasks.create'),
    path('tasks/<int:pk>', views.TasksDetailView.as_view(), name='tasks.detail'),
    path('tasks/<int:pk>/update', views.TasksUpdateView.as_view(), name='tasks.update'),
    path('tasks/<int:pk>/delete', views.TasksDeleteView.as_view(), name='tasks.delete'),
]