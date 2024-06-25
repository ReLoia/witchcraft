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
class User(BaseModel):
    username: str
    email: str
    password: str
    sandwitches: list[SandwitchItem]