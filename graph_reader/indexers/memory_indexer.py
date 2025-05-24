import glob
import json
import os
from typing import Any, List, Union

from .base_indexer import BaseIndexer
from .search_expression import (SearchExpression, SearchCondition,
                                SearchExpressionEvaluator, SearchOperator)


class MemoryIndexer(BaseIndexer):
    def __init__(self, base_dir):
        self.map = {}
        self.evaluator = SearchExpressionEvaluator()
        # Read all entity files and build the index
        entity_dir = os.path.join(base_dir, "entities")
        if os.path.exists(entity_dir):
            for file in glob.glob(os.path.join(entity_dir, "shard_*.jsonl")):
                with open(file, encoding="utf-8") as f:
                    for line in f:
                        entity = json.loads(line)
                        entity_id = entity["entity_id"]
                        self.map[entity_id] = entity["properties"]

    def search_by_property(
        self,
        key: str,
        value: Any,
        operation: str = "equals",
        case_sensitive: bool = True
    ) -> List[int]:
        """Search for entities by property value with various operations."""
        operator = SearchOperator(operation)
        condition = SearchCondition(key, operator, value, case_sensitive)
        return self.search(condition)

    def search(self, expression: Union[SearchExpression, SearchCondition]) -> List[int]:
        """Search for entities using a search expression."""
        return [
            eid
            for eid, props in self.map.items()
            if self.evaluator.evaluate_expression(expression, props)
        ]
