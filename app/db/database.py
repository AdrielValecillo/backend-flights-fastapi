from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

with open('app/secret.json') as f:
    env_vars = json.load(f)

# Replace the placeholders with your PostgreSQL connection details
db_user = env_vars['DB_USER']
db_password = env_vars['DB_PASSWORD']
db_host = env_vars['DB_HOST']
db_port = env_vars['DB_PORT']
db_name = env_vars['DB_NAME']

# Create the connection string
db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create the engine
engine = create_engine(db_url)

# Create the session
SessionLocal = sessionmaker(autocommit=False , autoflush=False, bind=engine)

# Create the base class
Base = declarative_base()