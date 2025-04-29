<p align="center">
  <img src="https://raw.githubusercontent.com/beanone/graph_builder/refs/heads/main/docs/assets/logos/banner.svg" alt="Graph Context Banner" width="100%">
</p>

A Python library for reading and querying graph data stored in JSONL format. The library provides efficient access to entity and relation data with support for different indexing strategies.

[![Python Versions](https://img.shields.io/pypi/pyversions/graph_builder)](https://pypi.org/project/graph_builder)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/beanone/graph_builder/blob/main/LICENSE)
[![Tests](https://github.com/beanone/graph_builder/actions/workflows/tests.yml/badge.svg)](https://github.com/beanone/graph_builder/actions?query=workflow%3Atests)
[![Coverage](https://codecov.io/gh/beanone/graph_builder/branch/main/graph/badge.svg)](https://codecov.io/gh/beanone/graph_builder)
[![Code Quality](https://img.shields.io/badge/code%20style-ruff-000000)](https://github.com/astral-sh/ruff)
[![PyPI version](https://img.shields.io/pypi/v/graph_builder)](https://pypi.org/project/graph_builder)


## Features

- Efficient reading of graph data from JSONL files
- Support for multiple indexing strategies (SQLite and Memory)
- Entity caching for improved performance
- Adjacency list-based neighbor lookup
- Property-based entity search
- Configurable cache size

## Architecture

The library is organized into the following components:

### Core Components

- `GraphReader`: Main class for reading and querying graph data
- `GraphReaderConfig`: Configuration class for customizing reader behavior

### Indexers

The library supports multiple indexing strategies through a plugin architecture:

- `BaseIndexer`: Abstract base class for indexers
- `SQLiteIndexer`: SQLite-based indexing for persistent storage
- `MemoryIndexer`: In-memory indexing for faster access

### Data Structure

The library expects data to be organized in the following directory structure:

```
base_dir/
├── entities/
│   └── shard_*.jsonl
├── relations/
│   └── shard_*.jsonl
└── adjacency/
    └── adjacency.jsonl
```

### Architecture Diagram

```mermaid
graph TD
    GR[GraphReader]
    GC[GraphReaderConfig]
    BI[BaseIndexer]
    SI[SQLiteIndexer]
    MI[MemoryIndexer]
    EF[Entity Files]
    RF[Relation Files]
    AF[Adjacency File]
    DB[(SQLite DB)]

    GR --> GC
    GR --> BI
    SI --> BI
    MI --> BI
    GR --> EF
    GR --> RF
    GR --> AF
    SI --> DB

    style GR fill:#e6f3ff,stroke:#000000,stroke-width:2px,color:#000000
    style GC fill:#e6f3ff,stroke:#000000,stroke-width:2px,color:#000000
    style BI fill:#fff2e6,stroke:#000000,stroke-width:2px,color:#000000
    style SI fill:#fff2e6,stroke:#000000,stroke-width:2px,color:#000000
    style MI fill:#fff2e6,stroke:#000000,stroke-width:2px,color:#000000
    style EF fill:#f0fff0,stroke:#000000,stroke-width:2px,color:#000000
    style RF fill:#f0fff0,stroke:#000000,stroke-width:2px,color:#000000
    style AF fill:#f0fff0,stroke:#000000,stroke-width:2px,color:#000000
    style DB fill:#f0fff0,stroke:#000000,stroke-width:2px,color:#000000
```

## Installation

```bash
pip install graph-reader
```

## Usage

```python
from graph_reader import GraphReader, GraphReaderConfig

# Initialize the reader with configuration
config = GraphReaderConfig(
    base_dir="path/to/graph/data",
    indexer_type="sqlite",  # or "memory"
    cache_size=1000
)
reader = GraphReader(config)

# Get entity by ID
entity = reader.get_entity("entity_id")

# Get neighbors of an entity
neighbors = reader.get_neighbors("entity_id")

# Search entities by property
matching_entities = reader.search_by_property("property_key", "property_value")
```

## Configuration

The `GraphReaderConfig` class supports the following parameters:

- `base_dir`: Base directory containing the graph data
- `indexer_type`: Type of indexer to use ("sqlite" or "memory")
- `cache_size`: Maximum number of entities to cache in memory

## License

This project is licensed under the MIT License - see the LICENSE file for details.