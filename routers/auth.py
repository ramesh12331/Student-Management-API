from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.user import User
from schemas.user import UserRegister, UserLogin
from security import hash_password ,verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user:UserRegister, con:Session = Depends(get_db)):
    existing_user = con.query(User).filter(User.username == user.username).first()

    if existing_user:
        return {
            "message": "Username already exists"
        }

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        username = user.username,
        email = user.email,
        password = hashed_password,
        role = "student"
    )
    con.add(new_user)
    con.commit()

    con.refresh(new_user)

    return{
        "message": "User registered successfully",
        "user_id": new_user.user_id,
        "username": new_user.username
    }


@router.post("/login")
def login(user:UserLogin, con:Session = Depends(get_db)):
    existing_user = con.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user is None:
        return {
            "message": "Invalid username or password"
        }

    password_correct = verify_password(
        user.password,
        existing_user.password
    )

    if not password_correct:
        return {
            "message": "Invalid username or password"
        }
    access_token = create_access_token({
        "sub": str(existing_user.user_id),
        "username": existing_user.username,
        "role": existing_user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }