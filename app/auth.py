from passlib.context import CryptContext
from fastapi import Depends,HTTPException
from app.model.user import User
from app.database import get_db
import jwt
from dotenv import load_dotenv
import os
from datetime import datetime,timedelta,timezone
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials


load_dotenv()

session=HTTPBearer()

exp_time=os. getenv("JWT_EXPIRE_TIME")
secret_key= os.getenv("JWT_SECRET_KEY")
algorithm= os.getenv("JWT_ALGORITHM")

crypt_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"

)

def make_hash(pwd:str) ->str:
    return crypt_context.hash(pwd)

def verify_hash(pwd,hash_pwd)->bool:
    return crypt_context.verify(pwd,hash_pwd)

def create_access_token(data:dict)-> str:
    payload=data.copy()

    exp=datetime.now(timezone.utc) + timedelta(
        minutes=int(exp_time)
    )

    payload["exp"]=exp

    return jwt.encode(
        payload,
        secret_key,
        algorithm
    )

def create_user_jwt(cred:HTTPAuthorizationCredentials=Depends(session),db = Depends(get_db)):
    token =cred.credentials
    try:
        data= jwt.decode(
            token,
            secret_key,
            algorithm
        )
        user= db.get(User,data["id"])
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="invalid token"
        )
    except jwt.InvalidSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Expired Token"
        )






