from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    recipes = relationship("Recipe", back_populates="user")
    likes = relationship("Like", back_populates="user")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')>"

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    instructions = Column(String)

    user = relationship("User", back_populates="recipes")
    ingredients = relationship("Ingredient", back_populates="recipe")
    likes = relationship("Like", back_populates="recipe")

    def __repr__(self) -> str:
        return f"<Recipe(id={self.id}, user_id={self.user_id}, instructions='{self.instructions}')>"

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    post_comments = Column(String)

    recipe = relationship("Recipe", back_populates="ingredients")

    def __repr__(self) -> str:
        return f"<Ingredient(id={self.id}, recipe_id={self.recipe_id}, post_comments='{self.post_comments}')>"

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    user = relationship("User", back_populates="likes")
    recipe = relationship("Recipe", back_populates="likes")

    def __repr__(self) -> str:
        return f"<Like(id={self.id}, user_id={self.user_id}, recipe_id={self.recipe_id})>"
