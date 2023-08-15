from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    auther: str
    image: str
    description: str
    publish_date: str
    description: str #| None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
        #orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    number: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    # is_active: bool
    # items: list[Item] = []

    class Config:
        from_attributes = True
        #orm_mode = True