from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from recipe import Post  

engine = create_engine('sqlite:///recipes.db')

Session = sessionmaker(bind=engine)
session = Session()

# Create a new post
new_post = Post(userid=2, postcomments='new photo ')

session.add(new_post)
session.commit()
session.close()
