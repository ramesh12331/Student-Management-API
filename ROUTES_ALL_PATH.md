Sure 👍 Here are **all the API routes/paths** in your current **Student Management API**, including Authentication.

Base URL:

```text
http://127.0.0.1:8000
```

# 📚 1. Student Routes

| Method | Path                | Purpose                | Auth |
| ------ | ------------------- | ---------------------- | ---- |
| GET    | `/students/`        | Get all students       | ❌    |
| GET    | `/students/profile` | Get authenticated user | 🔒   |
| GET    | `/students/{id}`    | Get student by ID      | ❌    |
| POST   | `/students/`        | Create student         | ❌    |
| PUT    | `/students/{id}`    | Update student         | ❌    |
| DELETE | `/students/{id}`    | Delete student         | ❌    |

### Examples

```text
GET    http://127.0.0.1:8000/students/
GET    http://127.0.0.1:8000/students/profile
GET    http://127.0.0.1:8000/students/1
POST   http://127.0.0.1:8000/students/
PUT    http://127.0.0.1:8000/students/1
DELETE http://127.0.0.1:8000/students/1
```

Your Swagger also shows the `/students/profile` endpoint under Students. 

---

# 📘 2. Course Routes

| Method | Path                  | Purpose                |
| ------ | --------------------- | ---------------------- |
| GET    | `/courses/`           | Get all courses        |
| POST   | `/courses/`           | Create course          |
| GET    | `/courses/{id}`       | Get course by ID       |
| PUT    | `/courses/{id}`       | Update course          |
| DELETE | `/courses/{id}`       | Delete course          |
| GET    | `/courses/{id}/marks` | Get marks for a course |

Examples:

```text
GET    http://127.0.0.1:8000/courses/
POST   http://127.0.0.1:8000/courses/
GET    http://127.0.0.1:8000/courses/1
PUT    http://127.0.0.1:8000/courses/1
DELETE http://127.0.0.1:8000/courses/1
GET    http://127.0.0.1:8000/courses/1/marks
```

---

# 📝 3. Marks Routes

| Method | Path             | Purpose                 |
| ------ | ---------------- | ----------------------- |
| GET    | `/marks/`        | Get all marks           |
| POST   | `/marks/`        | Create mark             |
| GET    | `/marks/{id}`    | Get mark by ID          |
| PUT    | `/marks/{id}`    | Update mark             |
| DELETE | `/marks/{id}`    | Delete mark             |
| GET    | `/marks/search/` | Get marks above minimum |

Examples:

```text
GET    http://127.0.0.1:8000/marks/
POST   http://127.0.0.1:8000/marks/
GET    http://127.0.0.1:8000/marks/1
PUT    http://127.0.0.1:8000/marks/1
DELETE http://127.0.0.1:8000/marks/1
GET    http://127.0.0.1:8000/marks/search/?minimum=80
```

---

# 📊 4. Report Routes

| Method | Path                                    | Purpose                    |
| ------ | --------------------------------------- | -------------------------- |
| GET    | `/reports/student-marks`                | Student + course + marks   |
| GET    | `/reports/student/{student_id}`         | One student's report       |
| GET    | `/reports/search/by-city`               | Students by city           |
| GET    | `/reports/search/`                      | Marks above minimum        |
| GET    | `/reports/students-with-marks`          | Students with marks        |
| GET    | `/reports/course-students`              | Courses + students + marks |
| GET    | `/reports/student-average/{student_id}` | Student average            |

Examples:

```text
GET http://127.0.0.1:8000/reports/student-marks

GET http://127.0.0.1:8000/reports/student/1

GET http://127.0.0.1:8000/reports/search/by-city?city=Hyderabad

GET http://127.0.0.1:8000/reports/search/?minimum=80

GET http://127.0.0.1:8000/reports/students-with-marks

GET http://127.0.0.1:8000/reports/course-students

GET http://127.0.0.1:8000/reports/student-average/1
```

These report paths are also shown in your Swagger document. 

---

# 🔐 5. Authentication Routes

| Method | Path             | Purpose               |
| ------ | ---------------- | --------------------- |
| POST   | `/auth/register` | Register new user     |
| POST   | `/auth/login`    | Login and receive JWT |

Your Swagger shows both authentication endpoints. 

### Register

```text
POST http://127.0.0.1:8000/auth/register
```

For your current standard OAuth2 login setup, login is:

```text
POST http://127.0.0.1:8000/auth/login
```

with:

```text
username = ravi
password = python123
```

Then you receive:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

---

# 🏠 6. Home Route

```text
GET http://127.0.0.1:8000/
```

Response:

```json
{
    "message": "Student Management API is Working"
}
```

---

# 🔑 Authentication Flow

Your current authentication-related routes are:

```text
POST /auth/register
       ↓
   Create User
       ↓
POST /auth/login
       ↓
   JWT Token 🔑
       ↓
GET /students/profile
       ↓
get_current_user()
       ↓
Authenticated ✅
```

---

# 📌 Complete Route List

```text
🏠 HOME
GET    /

👨‍🎓 STUDENTS
GET    /students/
GET    /students/profile 🔒
GET    /students/{id}
POST   /students/
PUT    /students/{id}
DELETE /students/{id}

📚 COURSES
GET    /courses/
POST   /courses/
GET    /courses/{id}
PUT    /courses/{id}
DELETE /courses/{id}
GET    /courses/{id}/marks

📝 MARKS
GET    /marks/
POST   /marks/
GET    /marks/{id}
PUT    /marks/{id}
DELETE /marks/{id}
GET    /marks/search/

📊 REPORTS
GET    /reports/student-marks
GET    /reports/student/{student_id}
GET    /reports/search/by-city
GET    /reports/search/
GET    /reports/students-with-marks
GET    /reports/course-students
GET    /reports/student-average/{student_id}

🔐 AUTHENTICATION
POST   /auth/register
POST   /auth/login
```

**🔒 Currently, `/students/profile` is the protected route.** The other CRUD routes are still public in the code you've built so far.
