from sqlalchemy import select, distinct

from modules.db_models.equity_prices import EquityPrices
from modules.db_models.equity_statics import EquityStatic

def get_latest_date(session):
    """
    Retrieve the maximum (latest) cob_date from the equity_prices table.

    :param session: SQLAlchemy session object.
    :return: The latest cob_date as a string (YYYY-MM-DD).
    :example:
        >>> from sqlmodel import create_engine
        >>> from sqlalchemy.orm import sessionmaker
        >>> DATABASE_URL = "sqlite:///equity_prices.db"
        >>> engine = create_engine(DATABASE_URL, echo=True)
        >>> SessionLocal = sessionmaker(bind=engine)
        >>> with SessionLocal() as session:
        ...     latest_date = get_latest_date(session)
    """
    latest_date = session.query(EquityPrices.cob_date).order_by(EquityPrices.cob_date.desc()).first()
    
    if latest_date:
        return latest_date[0]  # Extract date string from result tuple
    return None

def get_list_symbols(session):
    """
    Retrieve the the list of symbols for companies in db.

    :param session: SQLAlchemy session object.
    :return: a list of symbol ids for each company in database
    :example:
        >>> from sqlmodel import create_engine
        >>> from sqlalchemy.orm import sessionmaker
        >>> DATABASE_URL = "sqlite:///equity_prices.db"
        >>> engine = create_engine(DATABASE_URL, echo=True)
        >>> SessionLocal = sessionmaker(bind=engine)
        >>> with SessionLocal() as session:
        ...     latest_date = get_list_symbols(session)
    """
    query = select(distinct(EquityStatic.symbol))
    result = session.execute(query).scalars().all()
    
    if result:
        return result
    return list()
