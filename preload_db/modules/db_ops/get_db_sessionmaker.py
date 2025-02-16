from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_session(db_path: str):
    """
    Render a db session for sqlite db
    """
    try:
        engine = create_engine(db_path)
        return sessionmaker(bind=engine)
    except Exception as excp:
        print(f"Could not establish connection to database as {excp}")
        raise
