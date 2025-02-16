"""
Title: DB Loader -- Big Data in Quant Finance
=============================================

author: @uceslc0
description: ops helper to refresh data on regular basis
version date: 2025-02-15
"""
from ift_global import ReadConfig
from ift_global.utils.set_env_var import set_env_variables
import os

from modules.utils.local_logger import db_ops_logger
from modules.api_abstractions import get_key_statistics
from modules import (
    arg_parse_cmd,
    get_list_symbols,
    get_db_session
)
from modules.data_models import (
    GenericRapidApiRequest,
    SQLiteConfig,
)
from modules.db_models import CompanyStatistics


def main():
    db_ops_logger.info("Retrieve list of symbols from local database")
    Session = get_db_session(db_path=sqlite_config.path)
    with Session() as session:
        symbols_list = get_list_symbols(session=session)
    # example data_extraction_layer = "statistics"
    if parsed_args.request_type == "statistics":
        db_ops_logger.info("Perform Company Statistics requests")
        ra_static_conf = GenericRapidApiRequest(url=script_config["rapid_api"]["yh"]["stats_endpoint"],
                                                key=os.environ["RAPIDAPI_KEY"],
                                                host=script_config["rapid_api"]["yh"]["host_name"])
        database_models = list()
        for symbol in symbols_list:
            db_ops_logger.info(f"{symbol} Statistics requests starts")
            try:
                db_ops_logger.info(f"{symbol} Statistics requests to rapidapi")
                company_stats = get_key_statistics(symbol= symbol, rapidapi_conf=ra_static_conf)            
                database_models.append(CompanyStatistics(**company_stats.model_dump()))            
            except Exception as exc:
                print(f"While retriving company statics for company {symbol} an exception was raised")
                print(f"Exceptions : {exc}")
            db_ops_logger.info(f"{symbol} Statistics requests completed.")
        db_ops_logger.info(f"All Statistics requests are completed. Loading to sqlite database")
        SessionLocal = get_db_session(db_path=sqlite_config.path)
        with SessionLocal() as session:
            session.bulk_save_objects(database_models)
            session.commit()


if __name__ == "__main__":
    db_ops_logger.info("IFT BigData - DB OPS script started")
    args = arg_parse_cmd()
    parsed_args = args.parse_args()
    db_ops_logger.info("Reading configuration file from local properties folder.")
    # this would be equal to script_config = ReadConfig(env_type="dev")
    script_config = ReadConfig(env_type=parsed_args.env_type)
    sqlite_config = SQLiteConfig(path=script_config["database"]["sqlite"]["path"])
    # set env variables
    db_ops_logger.info("Setting env variables")
    set_env_variables(env_variables=["RAPIDAPI_KEY"], env_type="dev", env_file=parsed_args.secrets_env)
    main()
    db_ops_logger.info("IFT BigData - DB OPS script completed")
    
