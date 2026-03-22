import pytest

from dsa import Graph

# --- Constants ---
# Graph Structure
# 1 -- 2 -- 3
# |
# 4

NODES = [1, 2, 3, 4]
EDGES = [(1, 2), (2, 3), (1, 4)]

EXPECTED_BFS = [1, 2, 4, 3]
EXPECTED_DFS = [1, 2, 3, 4]
GRAPH_SIZE = len(NODES)


# --- Fixtures ---
@pytest.fixture
def empty_graph():
    """Return an empty graph."""
    return Graph()


@pytest.fixture
def populated_graph():
    """Return an undirected graph populated with NODES and EDGES."""
    g = Graph()
    for u, v in EDGES:
        g.add_edge(u, v, directed=False)
    return g


@pytest.fixture
def directed_graph():
    """Return a simple directed graph: 1 -> 2 -> 3."""
    g = Graph()
    g.add_edge(1, 2, directed=True)
    g.add_edge(2, 3, directed=True)
    return g


# --- Tests: Status & Utility ---
def test_is_empty(empty_graph, populated_graph):
    """Check is_empty property for empty and populated graphs."""
    assert empty_graph.is_empty is True
    assert populated_graph.is_empty is False


def test_size(empty_graph, populated_graph):
    """Verify size property returns the correct node count."""
    assert len(empty_graph) == 0
    assert len(populated_graph) == GRAPH_SIZE


# --- Tests: Modification Methods ---
def test_add_node(empty_graph):
    """Test adding nodes and ensuring idempotency (no duplicates)."""
    empty_graph.add_node("A")
    assert len(empty_graph) == 1

    empty_graph.add_node("A")
    assert len(empty_graph) == 1


def test_add_edge_directed_vs_undirected(empty_graph):
    """Test the difference between directed and undirected edge creation."""
    empty_graph.add_edge(1, 2, directed=False)
    assert empty_graph.has_edge(1, 2) is True
    assert empty_graph.has_edge(2, 1) is True

    empty_graph.add_edge(3, 4, directed=True)
    assert empty_graph.has_edge(3, 4) is True
    assert empty_graph.has_edge(4, 3) is False


def test_remove_node(populated_graph):
    """Test removing a node and cleaning up all associated connections."""
    populated_graph.remove_node(1)
    assert len(populated_graph) == 3
    assert populated_graph.has_edge(1, 2) is False

    assert 1 not in populated_graph.get_neighbors(2)
    assert 1 not in populated_graph.get_neighbors(4)


def test_remove_edge(populated_graph):
    """Test removing an edge while nodes remain in the graph."""
    populated_graph.remove_edge(1, 2, directed=False)
    assert populated_graph.has_edge(1, 2) is False
    assert populated_graph.has_edge(2, 1) is False
    assert len(populated_graph) == 4


# --- Tests: Access & Search Methods ---
def test_get_neighbors(populated_graph):
    """Verify get_neighbors returns correct values for existing and missing nodes."""
    neighbors = populated_graph.get_neighbors(1)
    assert set(neighbors) == {2, 4}

    assert populated_graph.get_neighbors(999) == []


def test_has_edge(populated_graph, directed_graph):
    """Test has_edge for various scenarios."""
    assert populated_graph.has_edge(1, 2) is True
    assert populated_graph.has_edge(1, 3) is False
    assert directed_graph.has_edge(2, 1) is False


# --- Tests: Traversal Methods (Deterministic) ---
def test_bfs_traversal(populated_graph):
    """Verify BFS returns nodes in a predictable level-order."""
    assert populated_graph.bfs(1) == EXPECTED_BFS


def test_dfs_traversal(populated_graph):
    """Verify DFS returns nodes in a predictable depth-first order."""
    assert populated_graph.dfs(1) == EXPECTED_DFS


def test_traversal_isolated_node():
    """Test traversal in a graph where a node has no neighbors."""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    assert g.bfs("A") == ["A"]
    assert g.dfs("A") == ["A"]


def test_traversal_empty_or_missing(empty_graph, populated_graph):
    """Ensure traversals handle empty graphs or missing start nodes gracefully."""
    assert empty_graph.bfs(1) == []
    assert populated_graph.bfs(999) == []


# --- Tests: Complex Scenarios ---
def test_cyclic_graph_traversal():
    """Verify that BFS/DFS don't get stuck in infinite loops in cyclic graphs."""
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    assert set(g.bfs(1)) == {1, 2, 3}
    assert set(g.dfs(1)) == {1, 2, 3}
