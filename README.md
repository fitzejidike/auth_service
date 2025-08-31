# 🚀 Django Authentication Service  

A simple but production-ready **User Authentication System** built with **Django**, **PostgreSQL**, **Redis**, and **JWT**, designed for modern backend systems.  
Includes Docker support, password reset with Redis cache, rate limiting for sensitive endpoints, and Swagger API documentation.  

---

## 📌 Features  

- 🔑 **User Registration & Login** (JWT-based authentication)  
- 📧 **Email as username** (no `username` field, only `email + password`)  
- 🔒 **Forgot/Reset Password** with Redis token (10 min expiry)  
- 🐳 **Dockerized** for easy local development  
- 🗄 **PostgreSQL** as main database  
- ⚡ **Redis** for caching password reset tokens  
- 🛡 **Rate limiting** on login & reset endpoints (prevents brute force attacks)  
- 📖 **Swagger UI docs** (auto-generated API docs)  

---

## 🏗 Project Structure  
auth_service/
├── auth_service/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── accounts/ # User authentication app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── .env.example
└── README.md

---

## ⚙️ Setup & Installation  

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/django-auth-service.git
cd django-auth-service
---


```markdown
## 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 3. Install dependencies

pip install -r requirements.txt


## 4.Set environment variables

Create a .env file (or set them in Render dashboard) with:

SECRET_KEY=<your-secret-key>
DEBUG=False
DATABASE_URL=<your-database-url>
# Optional if using Redis
REDIS_URL=<your-redis-url>


## 5.Run migrations

python manage.py migrate

## 6. Collect static files
python manage.py collectstatic --noinput

## 📄 API Endpoints

Swagger UI: /swagger/
Example: https://auth-service-os1u.onrender.com/swagger/

ReDoc UI: /redoc/
Example: https://auth-service-os1u.onrender.com/redoc/

Auth API: /api/auth/

POST /api/auth/register/ → Register a new user

POST /api/auth/login/ → Log in user and get JWT

GET /api/auth/profile/ → Get authenticated user profile

Full API documentation is available in Swagger/OpenAPI.

