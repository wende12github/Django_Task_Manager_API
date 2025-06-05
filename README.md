# Task Manager API

A simple REST API built with Django and Django REST Framework to manage tasks, stored in a JSON file. Supports CRUD operations, filtering by task status, and interactive API documentation via Swagger UI.

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository-url>
cd task_manager
```

### 2. Install Dependencies
Ensure Python is installed, then run:
```sh
pip install django djangorestframework drf-spectacular
```

### 3. Apply Migrations
```sh
python manage.py migrate
```

### 4. Create the `tasks.json` File
Create an empty `tasks.json` file in the project root directory:
```sh
echo "[]" > tasks.json
```

### 5. Run the Development Server
```sh
python manage.py runserver
```

## Access the API

- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the API status page.
- Visit [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/) to access the Swagger UI for interactive API documentation.

### API Endpoints

- `GET /api/tasks` — List all tasks
- `POST /api/tasks` — Create a task (e.g., `{"title": "Task 1", "description": "Details", "completed": false}`)
- `PUT /api/tasks/:id` — Update a task (mark as completed or edit)
- `DELETE /api/tasks/:id` — Delete a task
- Filter tasks: `GET /api/tasks?status=completed` or `GET /api/tasks?status=pending`

## Notes

- Task titles must not be empty (validation enforced).
- Data is stored in `tasks.json` in the project root.
- No database is required; a JSON file is used for simplicity.
- Swagger UI provides an interactive interface to test API endpoints at `/api/docs/`.