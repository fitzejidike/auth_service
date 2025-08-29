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



