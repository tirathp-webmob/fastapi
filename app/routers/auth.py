from fastapi import APIRouter, Depends,status,HTTPException, Response,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, oauth2, utils
from .. database import get_db
from ..schemas import UserLogin
router = APIRouter(tags=['Authenticate'])

@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first() #Fetches the whole data of 
                                                                                            #the user whose provided  #email id matches with the #one in database
    if not user:                        
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")

  
    if not utils.verify_pass(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id":user.id, "user_email":user.email})

    return {"access_token" : access_token, "token_type" : "bearer"}

