import kaggle
from prefect import task

"""
Place your kaggle.json file in the appropriate dir
Run $chmod 600 on: dir/kaggle.json
"""


@task
def extract():
    try:
        kaggle.api.authenticate()

        kaggle.api.dataset_download_files("ulrikthygepedersen/online-retail-dataset", path=".", unzip=True)
        print(f"Dataset downloaded and unzipped.")
    except Exception as e:
        print(f"An error occurred while downloading dataset: {e}")
