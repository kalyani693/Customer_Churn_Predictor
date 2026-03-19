from pydantic import BaseModel
from database_relational.db_main import sessionlocal


def get_db():
    db=sessionlocal()
    try: 
        yield db   
    finally:
        db.close()


