Sure 👍 For the **current step (Login + JWT)**, there is **no new installation** if you already installed the Phase 5 packages.

## 🔐 Phase 5 — JWT Installation

### 1. Activate your virtual environment

```bash
cd student_management_api
```

```bash
venv\Scripts\activate
```

You should see:

```text
(venv) ...
```

### 2. Install JWT package

If you haven't already installed it:

```bash
pip install python-jose[cryptography]
```

### 3. Password hashing package

Make sure this is also installed:

```bash
pip install passlib[bcrypt]
```

### 4. Install both at once

You can also simply run:

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

### 5. Update requirements

```bash
pip freeze > requirements.txt
```

### 6. Check installation

```bash
pip show python-jose
```

```bash
pip show passlib
```

You should see information for both packages.

### 7. Test imports

```bash
python -c "from jose import jwt; from passlib.context import CryptContext; print('JWT and Password Hashing are working!')"
```

Expected:

```text
JWT and Password Hashing are working!
```

---

### 📦 What each package does

```text
python-jose
     ↓
JWT Token
     ↓
Login authentication

passlib + bcrypt
     ↓
Password hashing
     ↓
Secure password storage
```

You are now ready for the next step: **protecting an API with JWT (`get_current_user`)**.

-------------
-------------
Great 👍 Now we move to the **most important authentication concept: Protected Routes**.

You already have:

```text
Register ✅
   ↓
Password Hashing ✅
   ↓
Login ✅
   ↓
JWT Token ✅
```

Now:

```text
JWT Token
   ↓
Verify Token
   ↓
Identify User
   ↓
Allow protected API ✅
```

# 🔐 STEP 16 — Protect APIs with JWT

We will create:

```python
get_current_user()
```

This function will check whether the user has a valid JWT token.

---

# 1️⃣ Update `security.py`

Open:

```text
security.py
```

Currently you have password hashing and JWT creation.

Now add these imports at the top:

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
```

Your imports become:

```python
from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
from jose import jwt, JWTError

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
```

---

# 2️⃣ Create OAuth2 scheme

Add:

```python
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)
```

### Why?

This tells FastAPI:

> The authentication token will come from the request's `Authorization` header, and the login endpoint is `/auth/login`.

The request will eventually look like:

```text
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

Think:

```text
Client
  ↓
Authorization Header
  ↓
Bearer JWT Token
  ↓
FastAPI
```

---

# 3️⃣ Create `get_current_user()`

Now add:

```python
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
```

---

# 🧠 Understand This Slowly

## Step 1 — Get the token

```python
token: str = Depends(oauth2_scheme)
```

FastAPI gets the token from:

```text
Authorization: Bearer <token>
```

For example:

```text
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

FastAPI extracts:

```text
eyJhbGciOiJIUzI1Ni...
```

and puts it into:

```python
token
```

---

# Step 2 — Decode JWT

```python
payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)
```

This checks whether the token is valid.

Remember we created the token using:

```python
jwt.encode(
    to_encode,
    SECRET_KEY,
    algorithm=ALGORITHM
)
```

Now we reverse the process:

```text
CREATE

data
 ↓
jwt.encode()
 ↓
JWT


VERIFY

JWT
 ↓
jwt.decode()
 ↓
data
```

---

# Step 3 — Get User ID

Our login code puts this inside the token:

```python
"sub": str(existing_user.user_id)
```

So the JWT contains information similar to:

```json
{
    "sub": "1",
    "username": "ravi",
    "role": "student",
    "exp": "..."
}
```

Then:

```python
user_id = payload.get("sub")
```

gets:

```text
1
```

---

# Step 4 — Check User ID

```python
if user_id is None:
```

If there is no user ID:

```text
❌ Invalid token
```

We return:

```python
raise HTTPException(
    status_code=401,
    detail="Invalid token"
)
```

### What is `401`?

HTTP `401` means:

> The request is not authenticated.

---

# Step 5 — Handle Invalid JWT

```python
except JWTError:
```

If the token is:

* invalid
* modified
* expired
* incorrectly signed

then JWT decoding can fail.

We return:

```python
raise HTTPException(
    status_code=401,
    detail="Invalid token"
)
```

---

# 4️⃣ Complete `security.py`

Now your complete file should look like this:

```python
from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext

from jose import jwt, JWTError

from fastapi import Depends, HTTPException

from fastapi.security import OAuth2PasswordBearer


# -------------------------
# JWT Settings
# -------------------------

SECRET_KEY = "my-super-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# -------------------------
# Password Hashing
# -------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# -------------------------
# Create JWT Token
# -------------------------

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# -------------------------
# OAuth2
# -------------------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# -------------------------
# Get Current User
# -------------------------

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
```

---

# 5️⃣ Create Your First Protected API

Now let's test authentication without changing your existing CRUD code.

Open:

```text
routers/students.py
```

Add:

```python
from security import get_current_user
```

So your imports will include:

```python
from security import get_current_user
```

---

# 6️⃣ Create `/profile`

Add this route:

```python
@router.get("/profile")
def student_profile(
    current_user = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user": current_user
    }
```

### Important ⚠️

Put `/profile` **before**:

```python
@router.get("/{id}")
```

For example:

```python
@router.get("/profile")
def student_profile(
    current_user = Depends(get_current_user)
):
    return {
        "message": "You are authenticated",
        "user": current_user
    }


@router.get("/{id}")
def get_student(
    id: int,
    db: Session = Depends(get_db)
):
    ...
```

Why?

Because otherwise FastAPI could interpret:

```text
/profile
```

as:

```text
/{id}
```

---

# 7️⃣ How Does `Depends()` Work Here?

This line is extremely important:

```python
current_user = Depends(get_current_user)
```

It means:

> Before executing `student_profile()`, run `get_current_user()`.

So:

```text
GET /students/profile
        ↓
get_current_user()
        ↓
Is JWT valid?
   ↓           ↓
  NO          YES
   ↓           ↓
  401       profile()
              ↓
           response
```

---

# 8️⃣ Test Without Login

Open:

```text
http://127.0.0.1:8000/docs
```

Find:

```text
GET /students/profile
```

Click **Execute**.

You have not provided a JWT token.

You should get something like:

```json
{
    "detail": "Not authenticated"
}
```

Why?

Because:

```text
No JWT
  ↓
No authentication
  ↓
❌ Access denied
```

---

# 9️⃣ Login First

Now use:

```text
POST /auth/login
```

Send:

```json
{
    "username": "ravi",
    "password": "python123"
}
```

You will receive:

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "token_type": "bearer"
}
```

Copy the **access_token**.

---

# 🔑 10️⃣ Authorize Swagger

At the top-right of Swagger, click:

```text
Authorize 🔒
```

Enter your token.

Depending on the Swagger UI authentication field, enter the token as:

```text
Bearer eyJhbGciOiJIUzI1NiIs...
```

Then click:

```text
Authorize
```

Now Swagger will send the token with protected requests.

---

# 11️⃣ Call `/students/profile` Again

Execute:

```text
GET /students/profile
```

Now you should get something similar to:

```json
{
    "message": "You are authenticated",
    "user": {
        "sub": "1",
        "username": "ravi",
        "role": "student",
        "exp": 178...
    }
}
```

🎉 Your first **protected API** is working.

---

# 🧠 Authentication Flow So Far

You have now built:

```text
                    REGISTER
                       ↓
                username/password
                       ↓
                 hash password
                       ↓
                   DATABASE
                       │
                       │
                       ↓
                     LOGIN
                       ↓
                verify password
                       ↓
                  create JWT
                       ↓
                 JWT TOKEN 🔑
                       │
                       ↓
              Authorization Header
                       ↓
              get_current_user()
                       ↓
                jwt.decode()
                       ↓
                 Valid token?
                 ↙          ↘
               NO            YES
               ↓              ↓
             401          Current User
                              ↓
                       Protected API
```

## 🎯 What you have learned

| Concept                 | Purpose                       |
| ----------------------- | ----------------------------- |
| `hash_password()`       | Securely hash passwords       |
| `verify_password()`     | Check login password          |
| `create_access_token()` | Create JWT                    |
| `OAuth2PasswordBearer`  | Read Bearer token             |
| `jwt.decode()`          | Verify/read JWT               |
| `get_current_user()`    | Authenticate request          |
| `Depends()`             | Run authentication before API |
| `401`                   | Authentication failed         |

### Next step

The next useful step is **Authorization**: we'll make `student` and `admin` users and learn how to allow certain APIs only to **admin users**.

