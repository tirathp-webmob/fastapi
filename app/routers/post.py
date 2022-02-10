
from operator import mod
from statistics import mode
from app import oauth2
from ..import models
from fastapi import Body, FastAPI, status, Depends, APIRouter, HTTPException, Response
from ..database import get_db
from ..schemas import PostCreate, PostOut, PostResponse, Post
from sqlalchemy.orm import Session
from sqlalchemy import func
import psycopg2
from psycopg2.extras import RealDictCursor
from decouple import config
import time
from typing import List, Optional

router = APIRouter(prefix="/posts", tags=['POSTS'])


# Get posts using SQLAlchemy.
@router.get("/", response_model=List[PostOut])
def get_posts(db: Session = Depends(get_db),
              user_id: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    posts = db.query(models.Post).filter(
        models.Post.email.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.email.contains(search)).limit(limit).offset(skip).all()
    return results


# Create posts using SQLAlchemy.
@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post_dict = models.Post(owner_id=user_id.id, **post.dict())
    db.add(post_dict)
    db.commit()
    db.refresh(post_dict)
    return post_dict

# Get single post using SQLALCHEMY


@router.get("/{id}", response_model=PostOut)
def get_posts(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).get(id)
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.      post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


    return post


# Delete post using SQLALCHEMY.
@router.delete("/{id}", response_model=PostResponse)
def delete(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).get(id)
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if post.owner_id != user_id.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden!! You are not authenticated user")
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update post using SQLALCHEMY
@router.put("/{id}", response_model=PostResponse)
def update(id: int, post: PostCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    updated_post = db.query(models.Post).filter(models.Post.id == id)

    new_post = updated_post.update(
        post.dict(), synchronize_session=False)

    if updated_post == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if updated_post.first().owner_id != user_id.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden!! You are not authenticated user")

    db.commit()
    return updated_post.first()
