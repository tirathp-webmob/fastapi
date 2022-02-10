
from jose import jwt, JWTError
from datetime import datetime, timedelta
from json import dumps
from . import schemas,models,database
from fastapi import Depends,HTTPException,status
from app import schemas
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def json_object(obj):
    if isinstance(obj, (datetime, timedelta)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = dumps(datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),default=json_object)

    to_encode.update({"expiration": expire})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token


def verify_token_access(token:str, credentials_exception):

    try:

        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate",
    headers={"WWW-Authenticate":"Bearer"})
     

    return verify_token_access(token,credentials_exception)