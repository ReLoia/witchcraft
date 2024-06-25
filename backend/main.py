from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# database
from sqlalchemy.orm import Session
from database import models
from database.session import get_db

# Models of FastAPI responses and handling
import models


app = FastAPI()

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
@app.post("/user", response_model=models.User)
async def create_user(user: models.User, db: Session = Depends(get_db)):
    # TODO(): Implement the database logic
    return user


# @app.get("/users/me", response_model=models.User)
# async def read_users_me(db: Session = Depends(get_db)):
#     # TODO(): Implement the database logic
#     return models.User(username="fakeuser", email="", password="", sandwitches=[])
