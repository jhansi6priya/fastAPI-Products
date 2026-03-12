#when connected to a server it is called a session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)
Session = sessionmaker(autocommit = False, autoflush=False, bind=engine)