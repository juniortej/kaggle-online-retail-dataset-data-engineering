import datetime
import os
import sys

from prefect import task
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import FloatType

sys.path.append(os.path.abspath("."))  # to run in my local rep.

from common_tools.constants import CREATE_AT, QUANTITY, SOURCE_FILE, TOTAL_PRICE, UNIT_PRICE


@task
def preprocessing(input_path: str, output_path: str):
    """
    Cleaned and transform raw data, save in a parquet file.

    :param input_path: path to raw data file
    :param output_path: path to where parquet file will be save.
    """
    spark_session = SparkSession.getActiveSession()
    data = spark_session.read.csv(input_path, header=True, inferSchema=True)
    data_cleaned = data.dropna().select(
        *(c for c in data.columns),
        (col(QUANTITY) * col(UNIT_PRICE)).alias(TOTAL_PRICE).cast(FloatType()),
        lit(input_path).alias(SOURCE_FILE),
        lit(datetime.datetime.now()).alias(CREATE_AT),
    )
    data_cleaned = data_cleaned.toDF(*[c.lower() for c in data_cleaned.columns])
    data_cleaned.write.parquet(output_path, mode="overwrite")

    print(f"Data cleaned and save in a csv file in {output_path}")
