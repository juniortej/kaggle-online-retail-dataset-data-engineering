import os
import sys

from prefect import flow

sys.path.append(os.path.abspath("."))  # to run in my local rep.

from common_tools.constants import CUSTOMERS_TABLE, PRODUCTS_TABLE, TRANSACTIONS_TABLE
from common_tools.spark import start_spark
from etl.preprocessing import preprocessing
from etl.processing import processing
from etl.write_to_postgres import create_tables, process_all_tables
from ingestion.extract import extract

app_name = "etl_kaggle_online_retail"
spark_session = start_spark(app_name)


def usage():
    print(
        """Argument required for this job: 
          - date file or time("hour") to process
          - input path file csv 
          - output path for parquet file"""
    )
    sys.exit()


@flow(log_prints=True)
def main():
    if not os.path.exists(input_path):
        print(f"The path {input_path} does not exist.\n We are going to download.")
        extract()
    preprocessing(input_path, output_path)
    dataframes = processing()
    create_tables()
    df_dict = {CUSTOMERS_TABLE: dataframes[0], PRODUCTS_TABLE: dataframes[-1], TRANSACTIONS_TABLE: dataframes[1]}

    table_names_dict = {
        CUSTOMERS_TABLE: CUSTOMERS_TABLE,
        PRODUCTS_TABLE: PRODUCTS_TABLE,
        TRANSACTIONS_TABLE: TRANSACTIONS_TABLE,
    }
    process_all_tables(df_dict, table_names_dict)


# --------------------#
#  APP STARTS HERE   #
# --------------------#
if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        main()
