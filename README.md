# University Grades API

![Tests](https://github.com/eddauren/university-grades/actions/workflows/tests.yml/badge.svg)

A small REST API I built while learning backend development.
It manages students, courses and grades. This is a learning project, not a production system.

## What I practiced

* SQL and PostgreSQL (joins, CTEs, window functions, transactions, upsert)
* Django and Django REST Framework
* REST API basics (HTTP methods, status codes, JSON errors, pagination)
* Token authentication and permissions
* Safe SQL (parameterized queries) and secrets in `.env`
* Tests with pytest
* Docker, docker-compose and GitHub Actions (CI)

## Features

* Add and list students, courses and enrollments
* Set a grade in one request (creates or updates)
* Find the best student of each course
* Anyone can read data, only staff can change it

## Endpoints

* `POST /api/token/` get a token
* `GET /api/students/` list students
* `GET /api/enrollments/` list enrollments
* `PUT /api/set-grade/` set a grade (staff only)
* `GET /api/top-students/` best student per course

## Run

Create a `.env` file (see `.env.example`), then:

```bash
docker compose up --build
```

The API is at `http://127.0.0.1:8000/api/`.
Run tests with `python -m pytest`.

## Notes

* `legacy/` has my first version: plain Python scripts with `psycopg`.
  `legacy/injection_demo.py` is an intentionally unsafe example of SQL injection.
* Not done yet: API docs (Swagger) and deployment.

**Tech:** Python, Django, DRF, PostgreSQL, pytest, Docker
