#when connected to a server it is called a session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#loads variables from a .env file
load_dotenv()

#import os is used to read env variables
DATABASE_URL = os.getenv("db_url")

#creates a connection to the database
#The engine is the core interface to the database
#python application -> SQLAlchemy engine -> DB
engine = create_engine(DATABASE_URL)

#creates a session object used to interact with the DB
#sessionmaker is a class used to generate DB sessions
SessionLocal = sessionmaker(
    autocommit=False, #manually must be committed by the user - so that changes are saved
    autoflush=False, #
    bind=engine #connects the session to the DB engine
)