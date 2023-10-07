from createRecipe import create_user, read_user, update_user, delete_user, create_recipe, read_recipe, update_recipe, delete_recipe
from createRecipe import create_ingredient,create_like
from recipe import User, Recipe,Ingredient,Like
from App import engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    inspector = inspect(engine)
    if not inspector.has_table("users"):
        User.__table__.create(bind=engine)

    if not inspector.has_table("recipes"):
        Recipe.__table__.create(bind=engine)

    # Create a new user
    new_user = create_user(session, first_name="Tobias", last_name="Og", email="tobiasog30@gmail.com")
    print(f"Created User: {new_user.first_name} {new_user.last_name}")
    
    new_recipe = create_recipe(session,user_id=new_user.id, instructions="Cook fish and fishmasala.")
    print(f"Created Recipe: {new_recipe}")

    user = read_user(session, new_user.id)
    recipe = read_recipe(session, new_recipe.id)
    
    if user and recipe:
        print(f"Read User: {user}")
        print(f"Read Recipe: {recipe}")

    # Update a user and a recipe
    update_user_data = {"email": "tobias0g99@gmail.com"}
    updated_user = update_user(session, new_user.id, update_user_data)

    update_recipe_data = {"instructions": "Cook fish and fishmasala, then add tomatoes."}
    updated_recipe = update_recipe(session, new_recipe.id, update_recipe_data)


    if updated_user and updated_recipe:
        print(f"Updated User: {updated_user}")
        print(f"Updated Recipe: {updated_recipe}")

   # Delete a user and a recipe
    user_deleted = delete_user(session, new_user.id)
    recipe_deleted = delete_recipe(session, new_recipe.id)


    if user_deleted and recipe_deleted:
        print("User and Recipe deleted successfully")

if __name__ == "__main__":
    # session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    inspector = inspect(engine)
    if not inspector.has_table("ingredients"):
        Ingredient.__table__.create(bind=engine)

    if not inspector.has_table("likes"):
       Like.__table__.create(bind=engine)

    # Create a new ingredient
    new_ingredient = create_ingredient(session, recipe_id=new_recipe.id, post_comments="Delicious fish recipe!")
    print(f"Created Ingredient: {new_ingredient}")

    # Create a new like
    new_like = create_like(session, user_id=new_user.id, recipe_id=new_recipe.id)
    print(f"Created Like: {new_like}")

    session.close()

