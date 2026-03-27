from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

#in password replace @ with %40 to avoid cofussion to computer

url_database=os.getenv("url_database")

engine= create_engine(url_database,echo=False)
sessionlocal= sessionmaker(autocommit=False,autoflush=False, bind=engine)
base=declarative_base()