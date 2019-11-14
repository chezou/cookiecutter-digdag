import os
import sys

os.system(f"{sys.executable} -m pip install -U pytd td-client")

import pytd

def run(database, table):
    apikey = os.environ["TD_API_KEY"]
    apiserver = os.environ["TD_API_SERVER"]
    client = pytd.Client(apikey=apikey, endpoint=apiserver)

    # Write your execution code
    return True
