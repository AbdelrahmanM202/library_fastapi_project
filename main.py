from fastapi import FastAPI,Depends, Request
from sqlalchemy.orm import Session
from library import models, schemas
from library.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Welcome to the Library"}


def get_db(request: Request):
    return request.state.db


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=schemas.UserBase)
def create_user(request: schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name=request.name,email=request.email,number=request.number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/users/')
def get_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get('/users/{id}')
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPExeption(status_code=status.HTTP_404_NOT_FOUND
                           ,detail=f"User with the id {id} is not available")
    return user


@app.put('/users/{id}')
def update_user(id:int,request: schemas.User, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.id == id).first()
    if existing_user:
        existing_user.name = request.name
        existing_user.email = request.email
        existing_user.number = request.number
        db.commit()
        db.refresh(existing_user)
        return {"message": f"User {id} updated"}
    else:
        raise HTTPException(status_code=404, detail="User not found")



@app.delete('/users/{id}')
def del_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    db.delete(user)
    db.commit()
    if not user:
        raise HTTPExeption(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")

    return {"message": "Deleted"}


@app.post('/books/', response_model=schemas.BookBase)
def create_book(request: schemas.Book, db: Session = Depends(get_db)):
    new_book = models.Book(title=request.title, author=request.author, image=request.image, description=request.description, publish_date=request.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get('/books/')
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books


@app.get('/books/{id}')
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPExeption(status_code=status.HTTP_404_NOT_FOUND
                               , detail=f"Book with the id {id} is not available")
    return book


@app.put('/books/{id}')
def update_book(id: int, request: schemas.Book, db: Session = Depends(get_db)):
    existing_book = db.query(models.Book).filter(models.Book.id == id).first()
    if existing_book:
        existing_book.title=request.title
        existing_book.author=request.author
        existing_book.image=request.image
        existing_book.description=request.description
        existing_book.publish_date=request.publish_date
        db.commit()
        db.refresh(existing_book)
        return {"message": f"User {id} updated"}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete('/books/{id}')
def del_book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    db.delete(book)
    db.commit()
    if not book:
        raise HTTPExeption(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with the id {id} is not available")
    return {"message": "Deleted"}
