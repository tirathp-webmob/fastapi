from trace import Trace
from typing import Collection
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, null
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=False)
    email = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete='CASCADE'), nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    phone_number = Column(String)


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer,ForeignKey("users.id",ondelete='CASCADE'),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete='CASCADE'),primary_key=True)