from main import session
from models import User, Comment
from sqlalchemy import select

statement = select(Comment).join(Comment.user).where(
    User.username == "jonnah"
).where(
    Comment.text == "Hello I'm jonnah"
)

result = session.scalars(statement).one()