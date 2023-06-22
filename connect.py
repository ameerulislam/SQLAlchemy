from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv('.env')

connection_string = os.getenv('DB_CONNECTION_STRING')
engine = create_engine(connection_string, echo=True)


with engine.connect() as connection:
    result = connection.execute(text('select \'Hello\''))
    print(result.all())