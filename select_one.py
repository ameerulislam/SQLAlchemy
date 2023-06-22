from main import session
from models import User

jonnah = session.query(User).filter_by(
    username = 'jonnah'
).first()

print (jonnah)