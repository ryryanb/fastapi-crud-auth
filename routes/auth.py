from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database import get_db
from crud import create_user, get_user_by_username
from schemas import UserCreate, UserResponse
from security import verify_password
from auth import create_access_token, verify_token
from datetime import timedelta
#from redis_client import redis
from redis.asyncio import Redis

# Create a Redis client instance
redis_client = Redis(decode_responses=True)  # Ensures stored values are strings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db, user)

async def store_token_in_redis(user: str, token: str, expire: int = 1800):
    """Stores token in Redis with expiration."""
    await redis_client.setex(f"token:{user}", expire, token)  # Fix: use `setex`

async def get_token_from_redis(user: str):
    """Retrieves token from Redis."""
    return await redis_client.get(f"token:{user}")

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Handles user login and token creation."""
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 🔹 Add `id` and `email` to the token payload
    token_payload = {
        "sub": user.username,
        "id": user.id,         # Add this
        "email": user.email    # Optional but recommended
    }

    token = create_access_token(token_payload, timedelta(minutes=30))
    await store_token_in_redis(user.username, token)  # Store token in Redis

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Retrieves current logged-in user based on token."""
    user_data = verify_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid token")

    return UserResponse(
        id=user_data["id"],          # Add this
        username=user_data["sub"],   # Already present
        email=user_data["email"]     # Add this
    )



