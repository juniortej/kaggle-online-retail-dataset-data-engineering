import datetime
import hashlib
from typing import List

from prefect import task
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, current_date, lit, udf
from pyspark.sql.types import FloatType, StringType, TimestampType

from common_tools.constants import (
    BASKET_ID,
    CREATE_AT,
    CREATION_DATEFILE,
    CUSTOMER_ALIAS,
    CUSTOMER_ID,
    PRODUCT_DESCRIPTION,
    PRODUCT_ID,
    PRODUCT_PRICE,
    QUANTITY,
    SOURCE_FILE,
    TOTAL_PRICE,
    TRANSACTION_DATETIME,
    UNIT_PRICE,
    UPDATE_AT,
)


# define an hash for aliases
def md5_hash(customer_id: str) -> str:
    return hashlib.md5(str(customer_id).encode()).hexdigest()


md5_udf = udf(md5_hash, StringType())


def read_parquet(directory_path: str) -> DataFrame:
    spark_session = SparkSession.getActiveSession()
    return spark_session.read.parquet(directory_path)


@task
def processing() -> List[DataFrame]:
    data = read_parquet("ingestion/file_retail.parquet")

    customers = data.select(
        col(CUSTOMER_ID).cast(StringType()),
        md5_udf(col(CUSTOMER_ID)).alias(CUSTOMER_ALIAS),
        col(SOURCE_FILE),
        col(CREATE_AT),
        lit(datetime.datetime.now()).cast(TimestampType()).alias(UPDATE_AT),
    ).distinct()
    # For next steps, we can update code to deal with new customers, merge...

    products = data.select(
        col("stockcode").alias(PRODUCT_ID),
        col("description").alias(PRODUCT_DESCRIPTION),
        col("unitprice").cast(FloatType()).alias(PRODUCT_PRICE),
        col(SOURCE_FILE),
        col(CREATE_AT),
        lit(datetime.datetime.now()).cast(TimestampType()).alias(UPDATE_AT),
    ).distinct()
    # For next steps, we can update code to deal with new products, merge...

    transactions_initial = data.select(
        col("invoiceno").alias(BASKET_ID),
        col("stockcode").alias(PRODUCT_ID),
        col("description").alias(PRODUCT_DESCRIPTION),
        col(QUANTITY.lower()).cast(FloatType()),
        col("invoicedate").alias(TRANSACTION_DATETIME),
        col("unitprice").alias(PRODUCT_PRICE),
        col(TOTAL_PRICE),
        col(CUSTOMER_ID).cast(StringType()),  # Joining on this field
        col("country"),
        col(SOURCE_FILE),
        lit(current_date()).alias(CREATION_DATEFILE),  # replace with datefile
        col(CREATE_AT),
    )

    transactions = transactions_initial.join(
        customers.select(CUSTOMER_ID, CUSTOMER_ALIAS), on=CUSTOMER_ID, how="left"
    ).drop(
        CUSTOMER_ID
    )  # try to be gdpr compliant :)

    return [customers, transactions, products]
