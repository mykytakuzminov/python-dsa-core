import pytest

from dsa import Graph

# Graph Structure
# 1 -- 2 -- 3
# |
# 4

NODES = [1, 2, 3, 4]
EDGES = [(1, 2), (2, 3), (1, 4)]

EXPECTED_BFS = [1, 2, 4, 3]
EXPECTED_DFS = [1, 2, 3, 4]
GRAPH_SIZE = len(NODES)


@pytest.fixture
def empty_graph():
    return Graph()


@pytest.fixture
def populated_graph():
    g = Graph()
    for u, v in EDGES:
        g.add_edge(u, v, directed=False)
    return g


@pytest.fixture
def directed_graph():
    g = Graph()
    g.add_edge(1, 2, directed=True)
    g.add_edge(2, 3, directed=True)
    return g


def test_is_empty(empty_graph, populated_graph):
    assert empty_graph.is_empty is True
    assert populated_graph.is_empty is False


def test_size(empty_graph, populated_graph):
    assert len(empty_graph) == 0
    assert len(populated_graph) == GRAPH_SIZE


def test_contains(empty_graph, populated_graph):
    assert 1 not in empty_graph
    assert 1 in populated_graph


def test_add_node(empty_graph):
    empty_graph.add_node("A")
    assert len(empty_graph) == 1

    empty_graph.add_node("A")
    assert len(empty_graph) == 1


def test_add_edge_directed_vs_undirected(empty_graph):
    empty_graph.add_edge(1, 2, directed=False)
    assert empty_graph.has_edge(1, 2) is True
    assert empty_graph.has_edge(2, 1) is True

    empty_graph.add_edge(3, 4, directed=True)
    assert empty_graph.has_edge(3, 4) is True
    assert empty_graph.has_edge(4, 3) is False


def test_remove_node(populated_graph):
    populated_graph.remove_node(1)
    assert len(populated_graph) == 3
    assert populated_graph.has_edge(1, 2) is False

    assert 1 not in populated_graph.get_neighbors(2)
    assert 1 not in populated_graph.get_neighbors(4)


def test_remove_non_existent_node(populated_graph):
    assert len(populated_graph) == 4
    populated_graph.remove_node(10)
    assert len(populated_graph) == 4


def test_remove_edge(populated_graph):
    populated_graph.remove_edge(1, 2, directed=False)
    assert populated_graph.has_edge(1, 2) is False
    assert populated_graph.has_edge(2, 1) is False
    assert len(populated_graph) == 4


def test_remove_non_existent_edge(populated_graph):
    populated_graph.remove_edge(10, 6, directed=False)
    assert len(populated_graph) == 4


def test_get_neighbors(populated_graph):
    neighbors = populated_graph.get_neighbors(1)
    assert set(neighbors) == {2, 4}

    assert populated_graph.get_neighbors(999) == []


def test_has_edge(populated_graph, directed_graph):
    assert populated_graph.has_edge(1, 2) is True
    assert populated_graph.has_edge(1, 3) is False
    assert directed_graph.has_edge(2, 1) is False


def test_bfs_traversal(populated_graph):
    assert populated_graph.bfs(1) == EXPECTED_BFS


def test_dfs_traversal(populated_graph):
    assert populated_graph.dfs(1) == EXPECTED_DFS


def test_traversal_isolated_node():
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    assert g.bfs("A") == ["A"]
    assert g.dfs("A") == ["A"]


def test_traversal_empty_or_missing(empty_graph, populated_graph):
    assert empty_graph.bfs(1) == []
    assert empty_graph.dfs(1) == []
    assert populated_graph.bfs(999) == []
    assert populated_graph.dfs(999) == []


def test_cyclic_graph_traversal():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    assert set(g.bfs(1)) == {1, 2, 3}
    assert set(g.dfs(1)) == {1, 2, 3}


def test_repr(empty_graph, populated_graph):
    assert repr(empty_graph) == "Graph([])"
    assert repr(populated_graph) == "Graph([1, 2, 3, 4])"


def test_str(empty_graph, populated_graph):
    assert str(empty_graph) == ""
    expected = "1 -> [2, 4]\n2 -> [1, 3]\n3 -> [2]\n4 -> [1]"
    assert str(populated_graph) == expected
