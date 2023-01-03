import os
from pathlib import Path

USER_API_KEY = os.environ['ALS_API_KEY']
API_REQ_TIMEOUT = 0.5
SQLITE_DB_PATH = Path.home() / 'apex_dt.db'
SQLITE_DB_URL = f'sqlite:///{SQLITE_DB_PATH}'

