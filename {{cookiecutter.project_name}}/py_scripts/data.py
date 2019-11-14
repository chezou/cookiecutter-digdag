import os
import sys
import pandas as pd

os.system(f"{sys.executable} -m pip install -U pytd td-client")

import pytd


# Modify or write you own code to fetch data
def prep_dataframe():
    df = pd.read_csv("/path/to/csv")
    return df

def upload_dataset(database, table):
    apikey = os.environ["TD_API_KEY"]
    apiserver = os.environ["TD_API_SERVER"]
    client = pytd.Client(apikey=apikey, endpoint=apiserver)

    client.create_database_if_not_exists(database)

    # Prepare your data in df variable
    df = prep_dataframe()

    # Upload dataframe to Treasure Data table
    client.load_table_from_dataframe(df, f"{database}.{table}", if_exists="overwrite")

    return True
