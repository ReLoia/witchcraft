from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# authentication import
import jwt
from database.auth.auth import authenticate_user, get_password_hash
from database.auth.security import create_access_token, decode_access_token

# database
from sqlalchemy.orm import Session
from database.models import UserEntity, SandwitchEntity
from database.session import get_db

# Models of FastAPI responses and handling
from models import SandwitchModel, UserModel, LoginTokenModel

app = FastAPI()

# authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# TODO: Add the correct origins
origins = [
    "http://localhost:5173",
    "localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


# Sandwitch API
@app.post("/sandwitch", response_model=SandwitchModel)
async def create_sandwitch(sandwitch: SandwitchModel, db: Session = Depends(get_db)):
    # TODO(): Implement the database logic
    return sandwitch


@app.get("/sandwitches", response_model=list[SandwitchModel])
async def get_sandwitches(db: Session = Depends(get_db)):
    sandwitches = db.query(SandwitchEntity).all()
    return sandwitches


# User API
@app.post("/token", response_model=LoginTokenModel)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_check = authenticate_user(db, form_data.username, form_data.password)
    if not auth_check:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": form_data.username})

    response = JSONResponse(content={"access_token": access_token, "token_type": "bearer"})
    response.set_cookie(key="access_token", value=access_token, httponly=True, max_age=60*60*24)

    return response


@app.post("/users", response_model=LoginTokenModel)
async def create_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    hashed_password = get_password_hash(form_data.password)

    new_user = UserEntity(username=form_data.username, hashed_password=hashed_password, sandwitches=[])
    db.query(UserEntity)
    if db.query(UserEntity).filter(UserEntity.username == form_data.username).first():
        return RedirectResponse(url="/token")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=UserModel)
async def get_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = db.query(UserEntity).filter(UserEntity.username == username).first()
    if user is None:
        raise credentials_exception

    return UserModel(username=user.username, sandwitches=[])

