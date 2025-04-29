"""Unit tests for the indexers/__init__.py module."""

import os

import pytest
from graph_builder.indexers import get_indexer
from graph_builder.indexers.memory_indexer import MemoryIndexer
from graph_builder.indexers.sqlite_indexer import SQLiteIndexer


@pytest.fixture
def test_dir(tmp_path):
    """Create a temporary directory for testing."""
    return str(tmp_path)


def test_get_indexer_sqlite(test_dir):
    """Test getting a SQLite indexer."""
    indexer = get_indexer("sqlite", test_dir)
    assert isinstance(indexer, SQLiteIndexer)
    # SQLiteIndexer doesn't store base_dir, it uses it to create the db path
    assert os.path.exists(os.path.join(test_dir, "index.db"))


def test_get_indexer_memory(test_dir):
    """Test getting a Memory indexer."""
    indexer = get_indexer("memory", test_dir)
    assert isinstance(indexer, MemoryIndexer)
    # MemoryIndexer doesn't store base_dir, it uses it to create the index path
    assert hasattr(indexer, "map")


def test_get_indexer_invalid_type(test_dir):
    """Test getting an invalid indexer type."""
    with pytest.raises(ValueError) as exc_info:
        get_indexer("invalid", test_dir)
    assert "Unknown indexer type: invalid" in str(exc_info.value)


def test_get_indexer_none_base_dir():
    """Test getting an indexer with None base_dir."""
    with pytest.raises(TypeError):
        get_indexer("sqlite", None)


def test_get_indexer_empty_base_dir():
    """Test getting an indexer with empty base_dir."""
    with pytest.raises(ValueError):
        get_indexer("sqlite", "")
