from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from recipe import Base


engine = create_engine('sqlite:///recipe_app.db')
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()
Base.metadata.create_all(engine)
