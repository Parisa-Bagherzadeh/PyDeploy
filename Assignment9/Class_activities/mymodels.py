from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    __table_args__ = {'extend_existing':True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: Optional[str]


class Message():
    __table_args__ = {'extend_existing':True}
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    type: str
    user_id: int = Field(default=None, foreign_key="user.id")