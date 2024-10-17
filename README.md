# Newsletter App

This project is a newsletter management application built with Django REST framework for the backend and Vue.js for the frontend. It enables users to create, manage, and send newsletters to their subscribers efficiently.

## Features

- **Admin Authentication**: JWT authentication system for admin users.
- **Email Delivery**: Celery and Redis are used to handle email sending processes efficiently.
- **Dockerized Environment**: The entire application runs in Docker, with the following containers:
  - `api`: Django REST Framework backend.
  - `db`: PostgreSQL database.
  - `web`: Frontend built with Vue.js.
  - `redis`: Redis for task queue management.
  - `celery`: Celery workers for processing email sending tasks.

## Backend

The backend of this project is built using Django REST Framework. Admin users authenticate using JWT tokens, and the system relies on Redis and Celery for handling email tasks.

### Key Technologies:
- Django REST Framework
- JWT Authentication
- Redis & Celery


## Frontend

The frontend of the newsletter application is built using **Vue 3 Composition API**. The design system was custom-built for this application, providing a consistent and reusable component library for UI elements.

### Key Technologies:
- **Vue 3 (Composition API)**: Core framework for building the app.
- **Axios**: HTTP client for making requests to the backend API.
- **Vuex**: Used for managing the application's state.
- **Vue Router**: Handles client-side routing between different views.
- **Vuelidate**: Library used for form validation.

## Environment Variables:

The following environment variables are located at `.env` file:

```env
POSTGRES_DB=newsletter_db
POSTGRES_USER=newsletter_user
POSTGRES_HOST=db
POSTGRES_LOCAL_PORT=15432
POSTGRES_PORT=5432
POSTGRES_PASSWORD=Adm1nP@ssw0rd!

API_WORKING_DIRECTORY=/api
API_NAME=api
API_HOST=0.0.0.0
API_LOCAL_PORT=8000
API_CONTAINER_PORT=8000
API_VERSION=1.0.0

WEB_WORKING_DIRECTORY=/web
WEB_NAME=web
WEB_HOST=0.0.0.0
WEB_LOCAL_PORT=5173
WEB_CONTAINER_PORT=5173
WEB_VERSION=1.0.0

REDIS_LOCAL_PORT=6379
REDIS_PORT=6379
CELERY_BROKER_URL=redis://redis/0

EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=password

API_BASE_URL=http://localhost:8000
WEB_BASE_URL=http://localhost:5173
```

The following environment variable is located at `/newsletter_frontend.env` file:

```env
VITE_API_URL=http://localhost:8000/api
```
## Execution Files

To build and run the application regularly, use the following script:

```bash
./run.bat
 ```

To build and run the application after installing npm dependencies, use the following script:

```bash
./run.bat
 ```