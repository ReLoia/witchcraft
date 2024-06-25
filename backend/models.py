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
# the data that will be sent to the client when they log in
class UserModel(BaseModel):
    username: str
    sandwitches: list[SandwitchItem]


class LoginTokenModel(BaseModel):
    access_token: str
    token_type: str
