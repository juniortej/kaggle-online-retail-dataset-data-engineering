from typing import List

import psycopg2
from prefect import task
from psycopg2.extras import execute_values
from pyspark.sql import DataFrame

from common_tools.constants import (
    BASKET_ID,
    CUSTOMER_ID,
    CUSTOMERS_TABLE,
    PRODUCT_ID,
    PRODUCTS_TABLE,
    TRANSACTION_DATETIME,
    UPDATE_AT,
)
from config.config import load_config


@task
def create_tables():
    # create tables in postgres db
    commands = (
        """
        CREATE TABLE IF NOT EXISTS  customers (
            customerid VARCHAR PRIMARY KEY,
            customer_alias VARCHAR,
            source_file VARCHAR,
            created_at TIMESTAMP,
            update_at TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS  products (
            product_id VARCHAR PRIMARY KEY,
            product_description VARCHAR,
            product_price FLOAT,
            source_file VARCHAR,
            created_at TIMESTAMP,
            update_at TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS  transactions (
            basket_id VARCHAR,
            product_id VARCHAR,
            product_description VARCHAR,
            quantity FLOAT,
            transaction_datetime TIMESTAMP,
            product_price FLOAT,
            total_price FLOAT,
            country VARCHAR,
            source_file VARCHAR,
            creation_datefile DATE,
            created_at TIMESTAMP,
            customer_alias VARCHAR
        )
        """,
    )

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Tables created successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error creating tables: {error}")


def open_db_connection():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        print("Connection to the PostgreSQL database was successful!")
        return conn, cursor
    except Exception as e:
        print("Error while connecting to the database:", e)
        raise


def close_db_connection(conn, cursor):
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Database connection closed.")
    except Exception as e:
        print("Error while closing the database connection:", e)


def merge_data_to_table(df, table_name, unique_columns, conn, cursor):
    """
    Merge data into the PostgreSQL table (Upsert).
    :param df: PySpark DataFrame containing the data.
    :param table_name: Target PostgreSQL table name.
    :param unique_columns: Columns that define uniqueness
    :param conn: PostgreSQL connection object.
    :param cursor: PostgreSQL cursor object.
    """
    try:
        columns = ",".join(df.columns)
        values_template = ",".join(["%s"] * len(df.columns))

        # Create the ON CONFLICT clause using unique columns for upsert
        conflict_columns = ",".join(unique_columns)
        update_clause = ", ".join([f"{col} = EXCLUDED.{col}" for col in df.columns if col not in unique_columns])

        query = f"""
        INSERT INTO {table_name} ({columns}) 
        VALUES ({values_template})
        ON CONFLICT ({conflict_columns}) 
        DO UPDATE SET {update_clause};
        """

        batch_size = 2000  # Can be adjusted. For memory optimization
        data_tuples = [tuple(x) for x in df.collect()]

        # Insert data in chunks
        for i in range(0, len(data_tuples), batch_size):
            chunk = data_tuples[i : i + batch_size]
            cursor.executemany(query, chunk)
            conn.commit()  # Commit after each chunk

        print(f"Data successfully merged into {table_name}!")

    except Exception as e:
        print(f"Error while merging data into {table_name}:", e)


@task
def process_all_tables(df_dict, table_names_dict):
    """
    Process all tables by merging data into them with a single connection.
    :param df_dict: Dictionary of PySpark DataFrames.
    :param table_names_dict: Dictionary of target table names for each DataFrame.
    """
    try:
        # Open a single connection for all operations
        conn, cursor = open_db_connection()

        for df, table_name in zip(df_dict.values(), table_names_dict.values()):
            if table_name == CUSTOMERS_TABLE:
                unique_columns = [CUSTOMER_ID]
            elif table_name == PRODUCTS_TABLE:
                unique_columns = [PRODUCT_ID]
            else:
                unique_columns = [BASKET_ID]

            merge_data_to_table(df, table_name, unique_columns, conn, cursor)

        print("All data successfully merged into their respective tables!")

    except Exception as e:
        print("Error during processing tables:", e)

    finally:
        close_db_connection(conn, cursor)
