from sqlalchemy import Column, Integer, String
from library.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    number = Column(String, unique=True, index=True)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    image = Column(String, index=True)
    description = Column(String, index=True)
    publish_date = Column(String, index=True)
