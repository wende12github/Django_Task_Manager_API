from django.urls import path
from tasks.views import TaskListView, TaskDetailView, index

urlpatterns = [
    path('', index, name='index'),
    path('api/tasks/', TaskListView.as_view(), name='task-list'),
    path('api/tasks/<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
]