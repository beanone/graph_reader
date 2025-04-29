"""Unit tests for the GraphReaderConfig class."""

import os
from pathlib import Path

import pytest
from graph_builder.config import GraphReaderConfig

# Get the test output directory
TEST_OUTPUT_DIR = Path(__file__).parent.parent.parent / "test_output"


def test_default_values():
    """Test that default values are set correctly."""
    config = GraphReaderConfig(base_dir=str(TEST_OUTPUT_DIR / "test1"))
    assert config.base_dir == str(TEST_OUTPUT_DIR / "test1")
    assert config.indexer_type == "sqlite"
    assert config.cache_size == 1000


def test_custom_values():
    """Test that custom values can be set."""
    config = GraphReaderConfig(
        base_dir=str(TEST_OUTPUT_DIR / "test2"), indexer_type="memory", cache_size=500
    )
    assert config.base_dir == str(TEST_OUTPUT_DIR / "test2")
    assert config.indexer_type == "memory"
    assert config.cache_size == 500


def test_required_base_dir():
    """Test that base_dir is required."""
    with pytest.raises(TypeError):
        GraphReaderConfig()


def test_invalid_cache_size():
    """Test that cache_size must be a positive integer."""
    with pytest.raises(ValueError):
        GraphReaderConfig(base_dir=str(TEST_OUTPUT_DIR / "test3"), cache_size=-1)


def test_empty_base_dir():
    """Test that base_dir cannot be empty."""
    with pytest.raises(ValueError):
        GraphReaderConfig(base_dir="")


def test_invalid_indexer_type():
    """Test that indexer_type must be either 'sqlite' or 'memory'."""
    with pytest.raises(ValueError):
        GraphReaderConfig(
            base_dir=str(TEST_OUTPUT_DIR / "test4"), indexer_type="invalid"
        )


def test_str_representation():
    """Test the string representation of the config object."""
    config = GraphReaderConfig(base_dir=str(TEST_OUTPUT_DIR / "test5"))
    str_repr = str(config)
    assert str(TEST_OUTPUT_DIR / "test5") in str_repr
    assert "sqlite" in str_repr
    assert "1000" in str_repr
