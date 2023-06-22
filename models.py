from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey,Text
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    email_address:Mapped[str]

class Comment(Base):
    __tablename__ = 'comments'
    id:Mapped[int] = mapped_column(primary_key=True)
    userid:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    text:Mapped[str] = mapped_column(Text, nullable=False)
