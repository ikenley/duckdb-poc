import logging
import duckdb
from duckdb_poc.config.logger_config import setup_logger

setup_logger()
logger = logging.getLogger(__name__)

logger.info("Open the pod bay doors, HAL")

# Example local script
# https://duckdb.org/docs/api/python/overview.html
# Raw data from https://www.mockaroo.com/
# Read CSV, transform, write to CSV

con = duckdb.connect(database=":memory:")

logger.info("Ingesting raw CSV")
raw_path = "./data/raw_data.csv"
con.execute(
    f"""create or replace table raw_film
    as from read_csv('{raw_path}', ignore_errors=true)"""
)
raw_film = con.table("raw_film")
raw_film.show()

logger.info("Transoforming table")
con.execute(
    f"""create or replace table transformed_film
    as select r.country
        , count(*) as number_of_films
    from {raw_film.alias} r
    group by r.country
    order by number_of_films desc"""
)
transformed_film = con.table("transformed_film")
transformed_film.show()

logger.info("Writing results to CSV")
output_csv_path = "./data/output.csv"
con.execute(f"""copy {transformed_film.alias} to '{output_csv_path}'""")
