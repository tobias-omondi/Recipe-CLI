from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from recipe import Recipe

engine = create_engine('sqlite:///recipes.db')
from recipe import Base
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

new_recipe = Recipe(firstName='Tobias', lastName='Omondi', profileName='tobiaschef', email='tobiasog21@gmail.com')
session.add(new_recipe)
session.commit()
