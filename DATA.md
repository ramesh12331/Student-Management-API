Sure 👍 Here are the **login details** for the user data we created earlier.

## 🔐 Login Data

### User 1 — Ravi

```json
{
    "username": "ravi",
    "password": "python123"
}
```

### User 2 — Priya

```json
{
    "username": "priya",
    "password": "fastapi123"
}
```

### User 3 — Amit

```json
{
    "username": "amit",
    "password": "sql12345"
}
```

### User 4 — Sneha

```json
{
    "username": "sneha",
    "password": "student123"
}
```

### User 5 — Arjun

```json
{
    "username": "arjun",
    "password": "python456"
}
```

## 🧪 Test in Swagger

Open:

```text
http://127.0.0.1:8000/docs
```

Select:

```text
POST /auth/login
```

For example, Ravi:

```json
{
    "username": "ravi",
    "password": "python123"
}
```

You should receive:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

### Then use the token 🔑

Click **Authorize 🔒** in Swagger and enter the token, then call:

```text
GET /students/profile
```

Expected:

```json
{
    "message": "You are authenticated",
    "user": {
        "sub": "1",
        "username": "ravi",
        "role": "student"
    }
}
```

**Important:** The database stores the hashed password, but you use the original password (`python123`, etc.) when logging in.
