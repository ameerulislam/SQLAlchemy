from models import User, Comment
from sqlalchemy.orm import Session
from connect import engine


session = Session(bind=engine)

jonnah = User(
    username = 'jonnah',
    email_address = 'jonna@example.com',
    comments = [
        Comment(text = "Hello I'm jonnah"),
        Comment(text = "Subscribe to my channel")
    ]
)

islam = User(
    username = 'islam',
    email_address = 'islam@example.com',
    comments = [
        Comment(text = "Hello I'm islam, howdy?"),
        Comment(text = "Subscribe to my channel")
    ]
)

khabib = User(
    username = 'khabib',
    email_address = 'khabib@example.com'
)

session.add_all([jonnah, islam, khabib])
session.commit()