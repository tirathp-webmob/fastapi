from ..import utils,models,schemas 
from fastapi import Body, FastAPI, status, Depends,APIRouter
from ..database import engine, get_db
from ..schemas import UserCreate,UserCreateResponse,Userget
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=['USERS'])
#Create Users
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=UserCreateResponse)
def createuser(user:UserCreate,db: Session = Depends(get_db)):
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd
    user_create = models.User(**user.dict())
    db.add(user_create)
    db.commit()
    db.refresh(user_create)

    return user_create


#Get users id
@router.get("/{id}",response_model=Userget)
def get_posts(id: int, db: Session = Depends(get_db)):
    post = db.query(models.User).get(id)
    return post
