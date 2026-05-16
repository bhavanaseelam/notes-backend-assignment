from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class NoteCreate(BaseModel):
    title: str
    content: str

class ShareNote(BaseModel):
    share_with_email: EmailStr