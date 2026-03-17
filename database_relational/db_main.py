from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#in password replace @ with %40 to avoid cofussion to computer
url_database="mysql+pymysql://root:Kalyani%40190306@localhost:3306/iiit_ngp_demo"

engine= create_engine(url_database,echo=False)
sessionlocal= sessionmaker(autocommit=False,autoflush=False, bind=engine)
base=declarative_base()