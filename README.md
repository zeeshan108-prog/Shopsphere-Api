# 🛒 ShopSphere API

A scalable E-commerce REST API built using Django and Django REST Framework.  
This project provides complete backend functionality for an online shopping platform including authentication, product management, cart system, and order processing.

---

## 🚀 Features

- User Registration & Login (JWT Authentication)
- Secure API Endpoints
- Product CRUD Operations (Admin Control)
- Category-wise Product Filtering
- Product Search Functionality
- Cart Management System
- Order Placement System
- RESTful API Architecture

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication
- SQLite (Default) / PostgreSQL

---

## 📂 Project Structure

```
shopsphere/
│── products/
│── orders/
│── users/
│── cart/
│── manage.py
│── requirements.txt
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/zeeshan108-prog/Shopsphere-Api.git
cd Shopsphere-Api
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```
python manage.py migrate
```

### 5️⃣ Run Server

```
python manage.py runserver
```

Server will start at:
```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication

This project uses JWT Authentication.

### Register User
```
POST /api/register/
```

### Login
```
POST /api/login/
```

After login, include the token in headers:

```
Authorization: Bearer <your_token>
```

---

## 📦 Main API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| GET | /api/products/ | List all products |
| POST | /api/products/ | Create product (Admin) |
| GET | /api/products/{id}/ | Product details |
| PUT | /api/products/{id}/ | Update product |
| DELETE | /api/products/{id}/ | Delete product |
| GET | /api/cart/ | View cart |
| POST | /api/orders/ | Place order |

---

## 🎯 Project Purpose

This project demonstrates practical backend development skills including:

- REST API Design
- Authentication & Authorization
- Database Modeling
- Business Logic Implementation
- Real-world E-commerce Workflow

---

## 👨‍💻 Author

Zeeshan Khan  
Backend Developer (Django | DRF)

---

⭐ If you found this project helpful, consider giving it a star!
