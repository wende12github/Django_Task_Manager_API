from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import TaskManager
from datetime import datetime

class TaskListView(APIView):
    def get(self, request):
        tasks = TaskManager.load_tasks()
        status_filter = request.query_params.get('status', None)
        if status_filter:
            if status_filter.lower() == 'completed':
                tasks = [task for task in tasks if task['completed']]
            elif status_filter.lower() == 'pending':
                tasks = [task for task in tasks if not task['completed']]
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            tasks = TaskManager.load_tasks()
            task_data = serializer.validated_data
            task_data['id'] = TaskManager.get_next_id(tasks)
            task_data['created_at'] = datetime.now().isoformat()
            tasks.append(task_data)
            TaskManager.save_tasks(tasks)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get_task(self, task_id):
        tasks = TaskManager.load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                return task
        return None

    def put(self, request, task_id):
        task = self.get_task(task_id)
        if not task:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            tasks = TaskManager.load_tasks()
            for i, t in enumerate(tasks):
                if t['id'] == task_id:
                    tasks[i] = {**t, **serializer.validated_data, 'id': task_id, 'created_at': t['created_at']}
                    TaskManager.save_tasks(tasks)
                    return Response(tasks[i])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        tasks = TaskManager.load_tasks()
        for i, task in enumerate(tasks):
            if task['id'] == task_id:
                tasks.pop(i)
                TaskManager.save_tasks(tasks)
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

def index(request):
    return render(request, 'tasks/index.html')