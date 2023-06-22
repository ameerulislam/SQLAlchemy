# SQLAlchemy
## sql Alchemy practice
Tutorial Source: https://www.youtube.com/watch?v=XWtj4zLl_tg
#### I'm using virtual environment for this practice

I had to edit pg_hba.conf to 
host    all             all             127.0.0.1/32            md5
from 
host    all             all             127.0.0.1/32            scram-sha-256

as it was giving me the following error
`sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "alchemy"`