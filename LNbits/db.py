import os
import sqlite3


LNBITS_PATH = os.path.dirname(os.path.realpath(__file__))
DEFAULT_PATH = os.path.join(LNBITS_PATH, "data", "database.sqlite3")


class Database:
    def __init__(self, db_path: str = DEFAULT_PATH):
        self.path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def fetchall(self, query: str, values: tuple) -> list:
        """Given a query, return cursor.fetchall() rows."""
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def execute(self, query: str, values: tuple) -> None:
        """Given a query, cursor.execute() it."""
        self.cursor.execute(query, values)
        self.connection.commit()