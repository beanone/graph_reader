import json
import os
from .base_indexer import BaseIndexer

class MemoryIndexer(BaseIndexer):
    def __init__(self, base_dir):
        self.map = {}
        index_path = os.path.join(base_dir, "memory_index.json")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                self.map = json.load(f)

    def search_by_property(self, key, value):
        return [eid for eid, v in self.map.items() if v == value]