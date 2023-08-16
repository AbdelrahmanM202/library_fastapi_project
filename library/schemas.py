from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    image: str
    description: str
    publish_date: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    email: str
    number: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int


    class Config:
        from_attributes = True
