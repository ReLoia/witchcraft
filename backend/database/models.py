from sqlalchemy import create_engine, Column, Integer, String, Boolean, Table
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./backend.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# association table for the many-to-many relationship between sandwitches and ingredients
sandwitch_ingredients = Table(
    "sandwitch_ingredients",
    Base.metadata,
    Column("sandwitch_id", Integer, sqlalchemy.ForeignKey("sandwitches.id"), primary_key=True),
    Column("ingredient_id", Integer, sqlalchemy.ForeignKey("ingredients.id"), primary_key=True)
)


# TODO: Add the models for the database
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    sandwitches = relationship("Sandwitch", back_populates="owner")


class Sandwitch(Base):
    __tablename__ = "sandwitches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String)
    likes = Column(Integer)
    owner_id = Column(Integer, sqlalchemy.ForeignKey("users.id"))
    owner = relationship("User", back_populates="sandwitches")
    ingredients = relationship("Ingredient", secondary=sandwitch_ingredients, back_populates="sandwitches")


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Integer)
    thickness = Column(Integer)
    size_width = Column(Integer)
    size_height = Column(Integer)
    image = Column(String)
    sandwitches = relationship("Sandwitch", secondary=sandwitch_ingredients, back_populates="ingredients")


Base.metadata.create_all(bind=engine)