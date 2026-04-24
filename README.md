# 🎓 University Management System API

A fully functional **full-stack** system built with **FastAPI** (backend) and a lightweight **HTML/CSS/JS** dashboard (frontend), featuring JWT authentication, role-based access control, and complete test coverage.

---

## 🚀 Features

- 🔐 JWT Authentication (Signup & Login)
- 🛡️ Role-Based Access Control (Admin, Faculty, etc.)
- 🔑 Admin Management (create, list, fetch, delete)
- 📚 Course Management
- 👨‍🎓 Student Management
- 👩‍🏫 Faculty Management
- 🔗 Enrollment System (Student ↔ Course)
- 🧪 Full API Test Suite with Pytest
- 🗄️ MySQL Database with SQLAlchemy ORM

---

## 🌐 Frontend (Basic Dashboard)

A simple frontend is included using **HTML, CSS, and JavaScript** to interact with the API.

### Features

- 🔐 Signup & Login
- 📚 Create Courses
- 👨‍🎓 Create Students
- 👩‍🏫 Create Faculty
- 🔗 Enrollment system
- 🛡️ Role-based access control (via backend)

### Notes

- This frontend is a **basic testing dashboard**, not a production UI.
- It helps visualize API interactions without tools like Postman.
- UI/UX improvements and React migration are planned.

### ▶️ Running Frontend

1. Start the backend server:

```bash
uvicorn app.main:app --reload
```

2. Open in browser:

```
frontend/index.html
```

### ⚠️ Security Note

- Role selection is handled **only by the backend**
- Frontend does **NOT** control permissions
- JWT tokens are required for all protected routes

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI 0.136.0 |
| Database | MySQL |
| ORM | SQLAlchemy 2.0.49 |
| Validation | Pydantic 2.13.2 |
| Authentication | JWT via python-jose 3.5.0 |
| Password Hashing | Passlib 1.7.4 (bcrypt 4.0.1) |
| Migrations | Alembic 1.18.4 |
| Testing | Pytest 9.0.3 |
| Server | Uvicorn 0.44.0 |
| HTTP Client | HTTPX 0.28.1 |

---

## 📁 Project Structure

```
University-Management/
│
├── backend/
│   └── app/
│       ├── main.py              # FastAPI app entry point
│       ├── core/                # Config, security, JWT logic
│       ├── db/                  # Database session & engine
│       ├── dependencies/        # FastAPI Depends() helpers
│       ├── migrations/          # Alembic migration scripts
│       ├── models/              # SQLAlchemy ORM models
│       ├── quires/              # Database query functions
│       ├── routes/              # API route handlers
│       ├── schemas/             # Pydantic request/response schemas
│       ├── services/            # Business logic layer
│       └── tests/               # Pytest test suite
│
├── frontend/
│   └── index.html               # Basic HTML/CSS/JS dashboard
│
├── .gitignore
├── .gitattributes
├── LICENSE                      # MIT License
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dhruv-Cmds/University-Management.git
cd University-Management
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the `backend/` directory:

```env
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=universitymanagement

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5️⃣ Create the database

Run this in your MySQL client:

```sql
CREATE DATABASE universitymanagement;
```

### 6️⃣ Run the server

```bash
cd backend
uvicorn app.main:app --reload
```

Visit the interactive API docs at:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication

All protected routes require a Bearer token in the request header:

```
Authorization: Bearer <your_token>
```

Admin signup and login are available at `POST /admin/signup` and `POST /admin/login`. See the [Admin endpoints](#-admin----admin) section above for details.

---

## 📡 API Endpoints Overview

> Full interactive documentation available at `/docs` (Swagger UI) and `/redoc`.

---

### 🔑 Admin — `/admin`

| Method | Endpoint | Auth Required | Role | Description |
|---|---|---|---|---|
| POST | `/admin/signup` | ❌ | — | Register a new admin |
| POST | `/admin/login` | ❌ | — | Login and receive JWT token |
| GET | `/admin/` | ✅ | `admin` | List all admins |
| GET | `/admin/{admin_id}` | ✅ | `admin` | Get admin by ID |
| DELETE | `/admin/{admin_id}` | ✅ | `admin` | Delete admin by ID |

**Schemas used:** `AdminCreate`, `AdminLogin`, `AdminResponse`

**Login response:**
```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

---

### 👨‍🎓 Students — `/students`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/students/` | ✅ | Create a new student |
| GET | `/students/` | ✅ | List all students |
| GET | `/students/{id}` | ✅ | Get student by ID |
| PUT | `/students/{id}` | ✅ | Update student |
| DELETE | `/students/{id}` | ✅ | Delete student |

---

### 👩‍🏫 Faculty — `/faculty`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/faculty/` | ✅ | Create a new faculty member |
| GET | `/faculty/` | ✅ | List all faculty |
| GET | `/faculty/{id}` | ✅ | Get faculty by ID |
| PUT | `/faculty/{id}` | ✅ | Update faculty |
| DELETE | `/faculty/{id}` | ✅ | Delete faculty |

---

### 📚 Courses — `/courses`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/courses/` | ✅ | Create a new course |
| GET | `/courses/` | ✅ | List all courses |
| GET | `/courses/{id}` | ✅ | Get course by ID |
| PUT | `/courses/{id}` | ✅ | Update course |
| DELETE | `/courses/{id}` | ✅ | Delete course |

---

### 🔗 Enrollments — `/enrollments`

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/enrollments/` | ✅ | Enroll a student in a course |
| GET | `/enrollments/` | ✅ | List all enrollments |
| DELETE | `/enrollments/{id}` | ✅ | Remove an enrollment |

---

## 🧪 Running Tests

```bash
cd backend
python -m pytest -v
```

- ✔ All endpoints tested
- ✔ Auth + RBAC included
- ✔ Database interactions validated

---

## 🧠 Key Concepts Implemented

- Clean architecture: `routes → services → queries → models`
- Dependency Injection via `FastAPI Depends()`
- Secure password hashing with bcrypt
- Token-based stateless authentication (JWT)
- Foreign key relationships and constraints in MySQL
- Database migrations with Alembic
- Test isolation with dynamic data generation

---

## 📦 Key Dependencies (from `requirements.txt`)

```
fastapi==0.136.0
uvicorn==0.44.0
sqlalchemy==2.0.49
alembic==1.18.4
pydantic==2.13.2
python-jose==3.5.0
passlib==1.7.4
bcrypt==4.0.1
pymysql==1.1.2
python-dotenv==1.2.2
httpx==0.28.1
pytest==9.0.3
email-validator==2.3.0
```

---

## 📌 Future Improvements

- ☁️ Deployment on Render / Railway
- ⚛️ React frontend migration
- 📊 Admin analytics dashboard
- 📧 Email notifications

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Dhruv** — [@Dhruv-Cmds](https://github.com/Dhruv-Cmds)

---

## ⭐ Acknowledgment

This project was built as part of backend development practice and demonstrates real-world API design, authentication, role-based access control, and testing workflows using modern Python tooling.
