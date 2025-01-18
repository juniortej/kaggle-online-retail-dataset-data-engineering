from pyspark.sql import SparkSession


def start_spark(app_name: str) -> SparkSession:
    spark_builder = SparkSession.builder.appName(app_name)
    spark_session: SparkSession = spark_builder.getOrCreate()
    return spark_session
