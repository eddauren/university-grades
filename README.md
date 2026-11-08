# University Grades API
 
![Tests](https://github.com/eddauren/university-grades/actions/workflows/tests.yml/badge.svg)
 
A small REST API I built while learning backend development.
It manages students, courses and grades. This is a learning project, not a production system.
 
**Live demo:** https://university-grades-vkyh.onrender.com/api/docs/
(free hosting, so the first request after a pause can take about a minute)
 
## What I practiced
 
* SQL and PostgreSQL (joins, CTEs, window functions, transactions, upsert)
* Django and Django REST Framework
* REST API basics (status codes, JSON errors, pagination)
* Token authentication and permissions
* Safe SQL (parameterized queries) and secrets in `.env`
* Tests with pytest
* Docker, GitHub Actions (CI) and deployment (Render, Neon)
## Features
 
* Students, courses and enrollments
* Set a grade in one request (creates or updates)
* Best student of each course
* Anyone can read data, only staff can change it
* API docs with Swagger at `/api/docs/`
## Run locally
 
Create a `.env` file (see `.env.example`), then:
 
```bash
docker compose up --build
```
 
The API is at `http://127.0.0.1:8000/api/`. Run tests with `python -m pytest`.
 
## Notes
 
`legacy/` has my first version: plain Python scripts with `psycopg`.
`legacy/injection_demo.py` is an intentionally unsafe example of SQL injection.
 
**Tech:** Python, Django, DRF, PostgreSQL, pytest, Docker