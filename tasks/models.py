from django.db import models
from django.conf import settings

import json
import os

class TaskManager:
    FILE_PATH = os.path.join(settings.BASE_DIR, 'tasks.json')

    @staticmethod
    def load_tasks():
        if not os.path.exists(TaskManager.FILE_PATH):
            return []
        with open(TaskManager.FILE_PATH, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_tasks(tasks):
        with open(TaskManager.FILE_PATH, 'w') as file:
            json.dump(tasks, file, indent=4)

    @staticmethod
    def get_next_id(tasks):
        return max([task['id'] for task in tasks], default=0) + 1