from sqlalchemy import create_engine


class BaseConnection:
    def __init__(self, db_path: str):
        self.db_path = db_path

    # Create an engine connected to an SQLite database
    # For an in-memory database
    @property
    def engine(self):
        return self._engine()
    def _engine(self):
        return create_engine(self.db_path)
    def get_engine(self):
        return self.engine
