from fastapi import APIRouter,Depends,HTTPException
from app.schemas.user import UserSchema,LoginSchema
from app .database import get_db
from app.model.user import User
from app.auth import make_hash,verify_hash,create_access_token


router=APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register")
def register(data:UserSchema,db=Depends(get_db)):
    user=User(
        name=data.name,
        email=data.email,
        role=data.role,
        password=make_hash(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/check")
def Check():
    return verify_hash("12345678","$2b$12$u1phHkuu/l4mrLCRCnpEpu1WV1IrNLOimLvgSS.NImAbyE.jakMnG")

@router.post("/login")
def login(cred: LoginSchema,db=Depends(get_db)):
    user=db.query(User).filter(User.email==cred.email).first()
    if not user:
        raise HTTPException(status_code=401,detail="invalid email")
    if not verify_hash(cred.password,user.password):
        raise HTTPException(status_code=401,detail="invalid password")
    
    token=create_access_token({"id":user.id,"role":user.role})

    return {
        "access_token":token,
        "token_type":"Bearer"
    }
