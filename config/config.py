import os

from dotenv import load_dotenv

load_dotenv()

# Params
PGHOST = os.getenv("PGHOST")
PGDATABASE = os.getenv("PGDATABASE")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
PGPORT = 5432  # default port for postgres


def load_config():
    return {"dbname": PGDATABASE, "user": PGUSER, "password": PGPASSWORD, "host": PGHOST, "port": PGPORT}
