# University Grades API

A small REST API for managing students, courses and grades.

> **This is a learning project.** I built it to practice the core skills of a
> junior Python backend developer. It is not used in production.

## Tech stack

Python, Django, Django REST Framework, PostgreSQL, pytest

## What it does

- Manage students, courses and enrollments (a student's grade in a course)
- Set a grade with one request: create the enrollment or update it if it exists
- Show the best student of each course (only courses with an average above 80)
- Token login. Anyone can read data, only staff users can change it


## Endpoints

| Method | URL | Description | Who |
|---|---|---|---|
| POST | `/api/token/` | Get an auth token | anyone |
| GET | `/api/students/` | List students (paginated) | anyone |
| POST | `/api/students/` | Create a student | staff |
| GET / POST | `/api/enrollments/` | List or create enrollments | read: anyone, write: staff |
| PUT | `/api/set-grade/` | Set a grade (`201` if created, `200` if updated) | staff |
| GET | `/api/top-students/` | Best student per course | anyone |


## Run locally

You need Python 3 and PostgreSQL.

1. Create a database named `university_api`.
2. Create a `.env` file in the project root:

   ```
   DJANGO_SECRET_KEY=your_secret_key
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   ```

3. Install and start:

   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\Activate.ps1   Linux/macOS: source .venv/bin/activate
   python -m pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```



## What I practiced

- **SQL and PostgreSQL:** joins, CTEs, window functions, indexes, transactions, upsert
- **Django and DRF:** models, migrations, serializers, viewsets, admin
- **REST API design:** HTTP methods, status codes, JSON errors, pagination
- **Security basics:** token authentication, permissions, secrets in `.env`,
  parameterized queries to prevent SQL injection
- **Data integrity:** constraints in the database and validation in the API
- **Testing:** pytest with fixtures, including tests for auth and error cases
- **Git and GitHub:** small commits, `.gitignore`, clear commit messages

## Project history

The project started as plain Python scripts talking to PostgreSQL with `psycopg`.
These early scripts are still in the repo root (`db.py`, `cli.py`,
`top_students.py`, `students.py`, `grades.py`).
`injection_demo.py` is an **intentionally vulnerable** example that shows
SQL injection next to the safe version.
Then I rebuilt the project as a Django REST API.

## What is not done yet

- Docker setup
- CI (automatic tests on every push)
- API documentation page (Swagger)
- Deployment
