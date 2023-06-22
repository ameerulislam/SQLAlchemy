from models import User, Comment
from main import session

# 1. Sepcific search
# statement = select(User).where(User.username.in_(['khabib', 'islam']))
# result = session.scalars(statement)
# for user in result:
#     print(user)

# 2. search all
users = session.query(User).all()
for user in users:
    print(user)