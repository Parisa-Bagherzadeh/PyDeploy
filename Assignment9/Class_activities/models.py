from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship


class User(SQLModel, table=True):
    __table_args__ = {'extend_existing' : True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: Optional[str]

    messages: list["Message"] = Relationship(back_populates="user")


class Message(SQLModel, table=True):  
    __table_args__ = {'extend_existing' : True}
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    type: str

    user_id: int = Field(default=None, foreign_key="user.id") 

    user: User = Relationship(back_populates="messages")

# ali = User()
# ali.messages

# m1 = Message()
# m1.user