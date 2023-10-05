from sqlalchemy import create_engine, Column ,String , ForeignKey ,Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# defination of database

class Recipe(Base):
    __tablename__ ="Recipe"
    userid = Column ("userid",Integer , primary_key = True)
    firstName = Column ("firstName", String)
    lastName = Column ("lasrName", String)
    profileName = Column ("profileName", String)
    email = Column ("email", String)

class Post(Base):
    __tablename__ ="Post"
    postid = Column ("postid" , Integer,primary_key=True)
    userid = Column ("userid", Integer, ForeignKey('Recipe.userid'))
    postcomments = Column ("postcomments", String)

class likes(Base):
    __tablename__ ="likes"
    likesid = Column ("likesid", Integer ,primary_key=True)
    userid = Column ("userid" ,Integer ,ForeignKey('Recipe.userid'))
    postid = Column ("postid" ,Integer , ForeignKey('Post.postid'))

# create recipe

