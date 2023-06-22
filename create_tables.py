from models import Base, User, Comment
from connect import engine

print("Creating Tasbles >>>>>")
Base.metadata.create_all(bind=engine)