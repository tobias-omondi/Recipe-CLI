# CRUD PART

# USERS
from sqlalchemy.orm import session
from recipe import User, Recipe, Ingredient, Like

def create_user(session,first_name, last_name, email):
    new_user = User(first_name=first_name, last_name=last_name, email=email)
    session.add(new_user)
    session.commit()
    return new_user

def read_user(session ,user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user

def update_user(session, user_id, new_data):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        for key, value in new_data.items():
            setattr(user, key, value)
        session.commit()
        return user
    else:
        return None

def delete_user(session, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    else:
        return False
    
    # RECIPE

def create_recipe(session, user_id, instructions):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        new_recipe = Recipe(user_id=user.id, instructions=instructions)
        session.add(new_recipe)
        session.commit()
        return new_recipe
    else:
        return None

def read_recipe(session, recipe_id):
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    return recipe

def update_recipe(session, recipe_id, new_data):
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        for key, value in new_data.items():
            setattr(recipe, key, value)
        session.commit()
        return recipe
    else:
        return None

def delete_recipe(session, recipe_id):
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if recipe:
        session.delete(recipe)
        session.commit()
        return True
    else:
        return False
    
# INGREDIENTS


def create_ingredient(session, recipe_id, post_comments):
    ingredient = Ingredient(recipe_id=recipe_id, post_comments=post_comments)
    session.add(ingredient)
    session.commit()

def get_ingredient_by_id(ingredient_id):
    return session.query(Ingredient).filter_by(id=ingredient_id).first()

def update_ingredient_comments(ingredient_id, new_comments):
    ingredient = get_ingredient_by_id(ingredient_id)
    if ingredient:
        ingredient.post_comments = new_comments
        session.commit()

def delete_ingredient(ingredient_id):
    ingredient = get_ingredient_by_id(ingredient_id)
    if ingredient:
        session.delete(ingredient)
        session.commit()

# Likes
def create_like(session, user_id, recipe_id):
    like = Like(user_id=user_id, recipe_id=recipe_id)
    session.add(like)
    session.commit()

def get_like_by_id(like_id):
    return session.query(Like).filter_by(id=like_id).first()

def update_like_user(user_id, like_id):
    like = get_like_by_id(like_id)
    if like:
        like.user_id = user_id
        session.commit()

def delete_like(like_id):
    like = get_like_by_id(like_id)
    if like:
        session.delete(like)
        session.commit()