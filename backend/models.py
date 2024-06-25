from pydantic import BaseModel


# Sandwitch models
class SandwitchIngredientSize(BaseModel):
    width: int
    height: int


class SandwitchIngredient(BaseModel):
    name: str
    amount: int
    thickness: int
    size: SandwitchIngredientSize
    image: str


class SandwitchItem(BaseModel):
    name: str
    image: str
    ingredients: list[SandwitchIngredient]
    likes: int


# User models
class LoginUserData(BaseModel):
    username: str
    password: str


# the data that will be sent to the client when they log in
class User(BaseModel):
    username: str
    sandwitches: list[SandwitchItem]
