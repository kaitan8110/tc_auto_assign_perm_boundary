# Need to pip3 install python-dotenv beforehand

import os
from dotenv import find_dotenv, load_dotenv

# find .env automatically by walking up directories until it's found
dotenv_path =  find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

SECRETID = os.getenv("SECRETID")
SECRETKEY = os.getenv("SECRETKEY")