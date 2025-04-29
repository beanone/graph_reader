import os
import sqlite3

from .base_indexer import BaseIndexer


class SQLiteIndexer(BaseIndexer):
    def __init__(self, base_dir):
        db_path = os.path.join(base_dir, "index.db")
        self.conn = sqlite3.connect(db_path)

    def search_by_property(self, key, value):
        cursor = self.conn.cursor()
        try:
            query = f"SELECT entity_id FROM entity_index WHERE {key} = ?"
            cursor.execute(query, (value,))
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.OperationalError:
            return []

    def __del__(self):
        if hasattr(self, "conn"):
            self.conn.close()
