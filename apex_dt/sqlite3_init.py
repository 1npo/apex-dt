"""Initialize the SQLite database the first time a new user uses the app."""

import sqlite3

from importlib import resources
from apex_dt.config import SQLITE_DB_PATH


with resources.path('apex_dt', 'sqlite3_schema.sql') as p:
    SQLITE_SCHEMA_PATH = p


def is_sqlite_db_empty() -> bool:
    """Check to see if the SQLite3 database is empty.

    :return: True if the database is empty, False if it's not
    :rtype: bool
    """
        
    con = sqlite3.connect(SQLITE_DB_PATH)
    cur = con.cursor()
    res = cur.execute('SELECT COUNT(*) FROM sqlite_schema;')
    
    if res.fetchone()[0] == 0:
        return False
    else:
        return True


def init_new_sqlite_db():
    """Initialize a new SQLite3 database from the provided schema."""
    con = sqlite3.connect(SQLITE_DB_PATH)
    cur = con.cursor()
    with open(SQLITE_SCHEMA_PATH, 'r') as f:
        cur.executescript(f.read())

    con.commit()


def sqlite_startup():
    """Create a new ApexDT SQLite3 database if one doesn't already exist."""
    if SQLITE_DB_FILE.is_file():
        if is_sqlite_db_empty() == False:
            return

    init_new_sqlite_db()

