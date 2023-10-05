from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from recipe import Likes 

engine = create_engine('sqlite:///recipes.db')

Session = sessionmaker(bind=engine)
session = Session()

# Create a new like and Replace 1 with actual user and post IDs

new_like = Likes(userid=1, postid=1)  

session.add(new_like)
session.commit()

session.close()
