"""Graph Reader - A library for reading graph data structures."""

__version__ = "0.1.0"

from .config import GraphReaderConfig
from .reader import GraphReader

__all__ = ["GraphReader", "GraphReaderConfig"]
