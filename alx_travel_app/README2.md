```markdown
# 🧳 ALX Travel App API

## 🌍 Overview

This project implements a RESTful API for managing **listings** and **bookings** using Django REST Framework. The API provides full CRUD operations for both models.

---

## ⚙️ Setup

### 🔁 Clone the repository:
```bash
git clone https://github.com/yourusername/alx_travel_app_0x01.git
cd alx_travel_app_0x01
```

### 📦 Install dependencies:
```bash
pip install -r requirements.txt
```

### 🛠 Apply migrations:
```bash
python manage.py migrate
```

### 🚀 Run the development server:
```bash
python manage.py runserver
```

---

## 🛣 API Endpoints

The API is accessible under `/api/`. Available endpoints:

### 📌 Listings
```http
GET    /api/listings/         - List all listings  
POST   /api/listings/         - Create a new listing  
GET    /api/listings/{id}/    - Retrieve a specific listing  
PUT    /api/listings/{id}/    - Update a specific listing  
DELETE /api/listings/{id}/    - Delete a specific listing  
```

### 📅 Bookings
```http
GET    /api/bookings/         - List all bookings  
POST   /api/bookings/         - Create a new booking  
GET    /api/bookings/{id}/    - Retrieve a specific booking  
PUT    /api/bookings/{id}/    - Update a specific booking  
DELETE /api/bookings/{id}/    - Delete a specific booking  
```

---

## 🧪 Testing

To test the API endpoints:

1. Use **Postman**, **Insomnia**, or any API client.
2. Set the base URL to:
```http
http://localhost:8000/api/
```
3. For `POST`, `PUT`, `DELETE` requests, include authentication headers if required.
4. Test each endpoint to verify CRUD functionality.

---

## 🧾 Swagger Documentation

Interactive API documentation is available at:

- Swagger UI:  
  ```http
  http://localhost:8000/api/schema/swagger-ui/
  ```

- ReDoc:  
  ```http
  http://localhost:8000/api/schema/redoc/
  ```

---

## 🔐 Authentication

- The API uses Django’s default **authentication system**.
- **Read operations** are open to all users.
- **Write operations** require user **authentication**.

---

## 📚 Dependencies

- `Django`
- `Django REST Framework`
- `drf-yasg` *(for Swagger docs)*

---

## 🗂 Project Structure

```
alx_travel_app/
├── listings/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── serializers.py
├── README.md
└── requirements.txt
```
```
