import os

import pytest
from fixture_generator import create_test_graph_fixture
from graph_builder.config import GraphReaderConfig
from graph_builder.reader import GraphReader


@pytest.fixture(scope="session")
def setup_graph_fixture(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("test_graph")
    create_test_graph_fixture(base_dir=temp_dir)
    return str(temp_dir)


@pytest.fixture(scope="module")
def reader(setup_graph_fixture):
    config = GraphReaderConfig(base_dir=setup_graph_fixture)
    return GraphReader(config)


def test_get_entity(reader):
    entity = reader.get_entity(1)
    assert entity is not None
    assert entity["entity_id"] == 1
    assert entity["properties"]["name"] == "Alice"


def test_get_neighbors(reader):
    neighbors = reader.get_neighbors(1)
    assert isinstance(neighbors, list)
    assert len(neighbors) == 1
    assert neighbors[0]["target_id"] == 2


def test_search_by_property(reader):
    results = reader.search_by_property("name", "Alice")
    assert isinstance(results, list)
    assert 1 in results


def test_get_entity_community(reader):
    community = reader.get_entity_community(1)
    assert community == "team_alpha"


def test_get_community_members(reader):
    members = reader.get_community_members("team_alpha")
    assert set(members) == {1, 2}
