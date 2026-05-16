from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, Text
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)

    password = Column(String)

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    content = Column(Text)

    owner_id = Column(Integer, ForeignKey("users.id"))

class SharedNote(Base):
    __tablename__ = "shared_notes"

    id = Column(Integer, primary_key=True, index=True)

    note_id = Column(Integer)

    shared_with_user_id = Column(Integer)