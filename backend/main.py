from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# authentication import
import jwt
from database.auth.auth import authenticate_user
from database.auth.security import create_access_token

# database
from sqlalchemy.orm import Session
from database import models
from database.session import get_db

# Models of FastAPI responses and handling
import models


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
@app.post("/sandwitch", response_model=models.SandwitchItem)
async def create_sandwitch(sandwitch: models.SandwitchItem, db: Session = Depends(get_db)):
    # TODO(): Implement the database logic
    return sandwitch


@app.get("/sandwitches", response_model=list[models.SandwitchItem])
async def get_sandwitches(db: Session = Depends(get_db)):
    # TODO(): Implement the database logic
    return []


# User API
@app.post("/token", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_check = authenticate_user(db, form_data.username, form_data.password)
    if not auth_check:
        return {"error": "Incorrect username or password"}

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users", response_model=models.User)
async def create_user(user: models.LoginUserData, db: Session = Depends(get_db)):
    hashed_password = "fakehashedpassword"

    # new_user = models.User(username=user.username, hashed_password=

    return {
        "username": user.username,
        "sandwitches": []
    }


# @app.get("/users/me", response_model=models.User)
# async def get_user(

