from dataclasses import dataclass


@dataclass
class GraphReaderConfig:
    """Configuration class for GraphReader.

    Attributes:
        base_dir: Base directory containing the graph data
        indexer_type: Type of indexer to use ('sqlite' or 'memory')
        cache_size: Maximum number of entities to cache in memory
    """

    base_dir: str
    indexer_type: str = "sqlite"
    cache_size: int = 1000

    VALID_INDEXER_TYPES = {"sqlite", "memory"}

    def __post_init__(self):
        """Validate configuration values after initialization."""
        if not self.base_dir:
            raise ValueError("base_dir cannot be empty")

        if self.indexer_type not in self.VALID_INDEXER_TYPES:
            raise ValueError(
                f"indexer_type must be one of {self.VALID_INDEXER_TYPES}, "
                f"got {self.indexer_type}"
            )

        if self.cache_size <= 0:
            raise ValueError("cache_size must be a positive integer")
