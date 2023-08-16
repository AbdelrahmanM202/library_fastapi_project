"""
from sqlalchemy.orm import Session

from library import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name,email=user.email,number=user.number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
"""