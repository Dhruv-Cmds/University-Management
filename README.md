# 🎓 University Management System API

A fully functional **full-stack University Management System** built with **FastAPI**, **MySQL**, and **Docker**, featuring JWT authentication, role-based access control, async database operations, and production-style API architecture.

The project includes a lightweight frontend dashboard built with **HTML/CSS/JavaScript** for testing and interacting with the API.

---

# 🚀 Features

- 🔐 JWT Authentication (Signup & Login)
- 🛡️ Role-Based Access Control (Admin, Faculty)
- ⚡ Async FastAPI + Async SQLAlchemy
- 🐳 Dockerized Backend & Database
- 📚 Course Management
- 👨‍🎓 Student Management
- 👩‍🏫 Faculty Management
- 🔗 Enrollment System
- 🧪 Full Async Pytest Suite
- 📈 k6 Load Testing & Benchmarking
- 🗄️ MySQL Database Integration
- 📄 Automatic Swagger/OpenAPI Documentation
- 🔒 Password Hashing with bcrypt
- 🚦 Rate Limiting using SlowAPI

---

# 🌐 Frontend Dashboard

A simple frontend dashboard is included using:

- HTML
- CSS
- JavaScript

It provides a lightweight UI to interact with the backend API.

---

## ✨ Frontend Features

- 🔐 Signup & Login
- 📚 Create Courses
- 👨‍🎓 Create Students
- 👩‍🏫 Create Faculty
- 🔗 Create Enrollments
- 🛡️ JWT Protected API Calls

---

## ⚠️ Frontend Notes

- This frontend is a **basic API interaction dashboard**
- It is **not intended as a production UI**
- React frontend migration is planned
- Authorization logic is handled entirely by the backend

---

# 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy 2.x |
| Async Driver | aiomysql |
| Validation | Pydantic |
| Authentication | JWT (python-jose) |
| Password Hashing | bcrypt + passlib |
| Testing | Pytest + pytest-asyncio |
| Load Testing | k6 |
| Server | Uvicorn |
| Containerization | Docker + Docker Compose |

---

# 📁 Project Structure

```text
University-Management/
│
├── backend/
│   ├── core/                # Config, JWT, security, limiter
│   ├── db/                  # Database engine & session
│   ├── dependencies/        # FastAPI dependencies
│   ├── migrations/          # Alembic migrations
│   ├── models/              # SQLAlchemy ORM models
│   ├── queries/             # Database query layer
│   ├── routes/              # API routes
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic layer
│   ├── tests/               # Async pytest suite
│   └── main.py              # FastAPI entrypoint
│
├── frontend/
│
├── docker/
│
├── requirements.txt
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# ⚙️ Local Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Dhruv-Cmds/University-Management.git

cd University-Management
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
COMPOSE_PROJECT_NAME=ums-app

DB_NAME=ums
TEST_DB_NAME=ums_test
DB_USER= ums_user
DB_PASSWORD=ums_password
MYSQL_ROOT_PASSWORD=ums_password

SECRET_KEY=yourkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 5️⃣ Create Database

```sql
CREATE DATABASE ums;
```

---

## 6️⃣ Run Backend

```bash
uvicorn backend.main:app --reload
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker Setup

## Run Full Stack

```bash
docker compose up --build
```

---

## Services

| Service | Port |
|---|---|
| FastAPI API | `8002` |
| MySQL | `3009` |

---

## API Docs

```text
http://localhost:8002/docs
```

---

# 🔐 Authentication

Protected routes require:

```text
Authorization: Bearer <your_token>
```

---

# 📡 API Endpoints

---

## 🔑 Admin — `/admin`

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/admin/signup` | ❌ | Register admin |
| POST | `/admin/login` | ❌ | Login and receive JWT |
| GET | `/admin/` | ✅ | List all admins |
| GET | `/admin/{admin_id}` | ✅ | Get admin by ID |
| DELETE | `/admin/{admin_id}` | ✅ | Delete admin |

---

## 📚 Courses — `/courses`

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/courses/` | ✅ | Create course |
| GET | `/courses/` | ✅ | List courses |
| GET | `/courses/{course_id}` | ✅ | Get course by ID |
| DELETE | `/courses/{course_id}` | ✅ | Delete course |

---

## 👨‍🎓 Students — `/students`

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/students/` | ✅ | Create student |
| GET | `/students/` | ✅ | List students |
| GET | `/students/{student_id}` | ✅ | Get student by ID |
| DELETE | `/students/{student_id}` | ✅ | Delete student |

---

## 👩‍🏫 Faculties — `/faculties`

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/faculties/` | ✅ | Create faculty |
| GET | `/faculties/` | ✅ | List faculties |
| GET | `/faculties/{faculty_id}` | ✅ | Get faculty by ID |
| DELETE | `/faculties/{faculty_id}` | ✅ | Delete faculty |

---

## 🔗 Enrollments — `/enrollments`

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/enrollments/` | ✅ | Create enrollment |
| GET | `/enrollments/` | ✅ | List enrollments |
| GET | `/enrollments/{enrollment_id}` | ✅ | Get enrollment by ID |
| DELETE | `/enrollments/{enrollment_id}` | ✅ | Delete enrollment |

---

# 🧪 Running Tests

Run async pytest suite:

```bash
pytest -v
```

---

## Test Coverage Includes

- JWT authentication
- Role-based access control
- CRUD operations
- Database integration
- Enrollment flow
- Protected routes
- Async route testing

---

# 🚀 Performance & Load Testing

The API was stress-tested using **k6** against a fully containerized environment:

- 🐳 FastAPI running in Docker
- 🐬 MySQL running in Docker
- ⚡ Async SQLAlchemy + aiomysql
- 🔐 JWT Authentication
- 🔑 bcrypt password hashing
- 🛡️ Rate limiting enabled
- 🧪 Mixed authenticated CRUD workloads

---

# 📊 Load Testing Results

| Test | Virtual Users | Duration | Requests/sec | Avg Latency | Success Rate |
|---|---|---|---|---|---|
| Admin Auth Load Test | 500 | 60s | ~388 req/s | ~781ms | 99.14% |
| Mixed API Load Test | 1000 | 60s | ~550 req/s | ~1.26s | 97.19% |
| Admin Signup Success | 1000 | 60s | Included Above | ~1.26s | 95% |
| Admin Login Success | 1000 | 60s | Included Above | ~1.26s | 98% |
| Dockerized Deployment Test | 1000 | 60s | ~550 req/s | ~1.26s | Stable |
| Sustained Concurrent Sessions | 1000 VUs | 60s | Stable Throughput | Minor Slowdown After ~700 VUs | System Responsive |

---

# ⚡ Scaling Behavior

| Concurrent Users | System Behavior |
|---|---|
| 1–200 Users | Very stable with low latency |
| 200–500 Users | Stable under heavy authenticated traffic |
| 500–700 Users | Minor latency increase, still responsive |
| 700–1000 Users | Bottlenecks begin appearing in bcrypt hashing and Docker networking |
| 1000+ Users | Temporary connection refusals and increased latency spikes |

---

# 🧠 Bottleneck Analysis

| Bottleneck | Cause |
|---|---|
| bcrypt hashing | CPU-intensive password hashing during signup/login |
| Docker Desktop networking | Windows Docker bridge overhead under high concurrency |
| Single-machine MySQL container | Concurrent write pressure |
| TCP/socket exhaustion | Windows localhost socket limitations during extreme load |

---

# 🐧 Linux Deployment Expectations

The benchmarks above were executed on:

- Windows
- Docker Desktop
- Localhost networking
- Single machine setup

Deploying on Linux infrastructure is expected to significantly improve performance.

---

## Expected Linux Improvements

| Optimization | Expected Improvement |
|---|---|
| Native Linux networking | Lower latency |
| Gunicorn + multiple workers | Higher throughput |
| Dedicated database instance | Better concurrent write handling |
| Reverse proxy (Nginx) | Improved connection management |
| Production-grade VPS hardware | Better bcrypt performance |

---

# 🏗️ Stability Summary

| Metric | Result |
|---|---|
| Total Requests Processed | 35,020 |
| Maximum Concurrent Virtual Users Tested | 1000 |
| Interrupted Iterations | 0 |
| Full System Crashes | 0 |
| Database Failures | None Observed |
| Event Loop Failures | None Observed |
| Container Stability | Stable Throughout Sustained Load |

---

# 🧪 k6 Benchmarking

Run load tests:

```bash
k6 run load_test.js
```

Benchmark suite includes:

- Admin signup/login
- JWT generation
- Course creation
- Student creation
- Faculty creation
- Enrollment creation
- Authenticated GET endpoints
- Concurrent database writes
- Protected role-based routes

---

# 🔥 Production Deployment

Recommended production command:

```bash
gunicorn backend.main:app \
  -k uvicorn.workers.UvicornWorker \
  -w 4 \
  -b 0.0.0.0:8000
```

---

## Recommended Production Stack

- Linux VPS
- Gunicorn + Uvicorn workers
- Nginx reverse proxy
- Docker Compose
- Managed MySQL/PostgreSQL
- Redis caching (future improvement)

---

# 🧠 Architecture Highlights

- Clean architecture:
  ```text
  routes → services → queries → models
  ```

- Dependency Injection using FastAPI
- Async database operations
- Stateless JWT authentication
- Foreign key constraints
- Service-layer business logic
- Async test isolation
- Dockerized infrastructure

---

# 📦 Core Dependencies

```text
fastapi
sqlalchemy
aiomysql
uvicorn
pydantic
python-jose
passlib
bcrypt
pytest
pytest-asyncio
httpx
slowapi
docker
```

---

# 📌 Future Improvements

- ⚛️ React frontend migration
- 📊 Admin analytics dashboard
- 📧 Email notifications
- ☁️ Cloud deployment
- 🔄 Refresh tokens
- 📈 Prometheus + Grafana monitoring
- 🧠 Redis caching
- 🔔 WebSocket notifications

---

# 📄 License

Licensed under the MIT License.

---

# 👤 Author

**Dhruv**  
GitHub: https://github.com/Dhruv-Cmds

---

# ⭐ Acknowledgment

This project was built as a real-world backend engineering practice project demonstrating:

- API architecture
- JWT authentication
- RBAC authorization
- async FastAPI patterns
- Dockerized deployment
- database integration
- load testing
- production-style backend design

---