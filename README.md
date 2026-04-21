# 🎓 University Management System API

A fully functional backend system built with **FastAPI**, featuring authentication, role-based access control, and complete test coverage.

---

## 🚀 Features

* 🔐 JWT Authentication (Signup & Login)
* 🛡️ Role-Based Access Control (Admin, Faculty, etc.)
* 📚 Course Management
* 👨‍🎓 Student Management
* 👩‍🏫 Faculty Management
* 🔗 Enrollment System (Student ↔ Course)
* 🧪 Full API Test Suite with Pytest
* 🗄️ MySQL Database with SQLAlchemy ORM

---
## 🌐 Frontend (Basic Dashboard)

A simple frontend is included using **HTML, CSS, and JavaScript** to interact with the API.

### Features

* 🔐 Signup & Login
* 📚 Create Courses
* 👨‍🎓 Create Students
* 👩‍🏫 Create Faculty
* 🔗 Enrollment system
* 🛡️ Role-based access control (via backend)

### Notes

* This frontend is a **basic testing dashboard**, not a production UI.
* It helps visualize API interactions without tools like Postman.
* UI/UX improvements and React migration are planned.

---

## ▶️ Running Frontend

1. Start backend server:

```bash
uvicorn app.main:app --reload
```

2. Open:

```text
frontend/index.html
```

---

## ⚠️ Security Note

* Role selection is handled **only by backend**
* Frontend does NOT control permissions
* JWT tokens are required for protected routes


## 🏗️ Tech Stack

* **Backend:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Authentication:** JWT (python-jose)
* **Testing:** Pytest
* **Password Hashing:** Passlib (bcrypt)

---

## 📁 Project Structure

```
university-system/
│
├── app/
│   ├── main.py
│   ├── core/
│   ├── db/
│   ├── dependencies/
│   ├── migrations/
│   ├── models/
│   ├── quires/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── tests/
│
│
│
├── .env
├── requirements.txt
└── README.md
 
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd university-system
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Create a `.env` file:

```env
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=universitymanagement

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 5️⃣ Create database manually

```sql
CREATE DATABASE universitymanagement;
```

---

### 6️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication

### Signup

```
POST /auth/signup
```

### Login

```
POST /auth/login
```

Returns:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

Use token in headers:

```
Authorization: Bearer <token>
```

---

## 🧪 Running Tests

```bash
python -m pytest -v
```

✔ All endpoints are tested
✔ Auth + RBAC included
✔ Database interactions validated

---

## 🧠 Key Concepts Implemented

* Clean architecture (routes → services → models)
* Dependency Injection (FastAPI Depends)
* Secure password hashing
* Token-based authentication
* Foreign key relationships & constraints
* Test isolation with dynamic data

---

## 📌 Future Improvements
* ☁️ Deployment (Render / Railway)
---

## 👤 Author

**Your Name**

---

## ⭐ Acknowledgment

This project was built as part of backend development practice and demonstrates real-world API design, authentication, and testing workflows.
