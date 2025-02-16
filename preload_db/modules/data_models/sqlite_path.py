from pydantic import BaseModel, AfterValidator, Field
from pydantic.networks import UrlConstraints
from typing_extensions import Annotated, TypeAlias

def check_sqlite_path(path: str) -> str:
    if path.startswith("sqlite:///"):
        return path
    raise ValueError("SQLite path is not formatted correctly as: 'sqlite:///'")

SQLitePath: TypeAlias = Annotated[str, AfterValidator(check_sqlite_path)]


class SQLiteConfig(BaseModel):
    path: SQLitePath = Field(..., description="The sqlite file path as 'sqlite:///'")

