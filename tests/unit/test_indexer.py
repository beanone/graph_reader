# tests/unit/test_indexer.py
import os
import sqlite3

import pytest
from fixture_generator import create_test_graph_fixture
from graph_builder.indexers.memory_indexer import MemoryIndexer
from graph_builder.indexers.sqlite_indexer import SQLiteIndexer


@pytest.fixture(scope="session")
def setup_graph_fixture(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("test_graph")
    create_test_graph_fixture(base_dir=temp_dir)
    return str(temp_dir)


@pytest.fixture(scope="session")
def setup_sqlite_db(setup_graph_fixture):
    """Setup SQLite database with test data."""
    db_path = os.path.join(setup_graph_fixture, "index.db")

    # Remove existing db if any
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS entity_index (
            entity_id INTEGER,
            name TEXT,
            type TEXT,
            community_id TEXT
        )
    """
    )

    test_data = [
        (1, "Alice", "Person", "team_alpha"),
        (2, "Bob", "Person", "team_alpha"),
        (3, "Charlie", "Person", "team_beta"),
    ]

    cursor.executemany(
        "INSERT OR REPLACE INTO entity_index (entity_id, name, type, community_id) VALUES (?, ?, ?, ?)",
        test_data,
    )
    conn.commit()
    conn.close()

    yield setup_graph_fixture  # Return the base_dir as SQLiteIndexer expects it

    # Cleanup after all tests
    if os.path.exists(db_path):
        os.remove(db_path)


class BaseIndexerTest:
    """Base test class for all indexer implementations."""

    @pytest.fixture(scope="module")
    def indexer(self, setup_graph_fixture):
        """Should be overridden by subclasses to provide specific indexer instance."""
        raise NotImplementedError

    # ... rest of the test methods remain the same ...


class TestMemoryIndexer(BaseIndexerTest):
    """Test class for MemoryIndexer implementation."""

    @pytest.fixture(scope="module")
    def indexer(self, setup_graph_fixture):
        return MemoryIndexer(setup_graph_fixture)


class TestSQLiteIndexer(BaseIndexerTest):
    """Test class for SQLiteIndexer implementation."""

    @pytest.fixture(scope="module")
    def indexer(self, setup_sqlite_db):
        return SQLiteIndexer(setup_sqlite_db)
