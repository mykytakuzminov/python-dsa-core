from __future__ import annotations

from typing import Any, Protocol, TypeVar

from .queue import Queue
from .stack import Stack


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


class Node[T: Comparable]:
    """
    A node in a graph.

    Attributes:
        value: The data stored in the node.
        neighbors: A set of references to neighboring Node objects.
    """

    value: T
    neighbors: set[Node[T]]

    def __init__(self, value: T):
        """Initialize a graph node."""
        self.value = value
        self.neighbors = set()

    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"Node({self.value})"


class Graph[T: Comparable]:
    """
    Graph implementation using an adjacency list.

    Attributes:
        _adj_list: Dictionary mapping values to their corresponding Node objects.
    """

    _adj_list: dict[T, Node[T]]

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self._adj_list = {}

    def __len__(self) -> int:
        """Return the total number of nodes in the graph."""
        return len(self._adj_list)

    def __contains__(self, value: T) -> bool:
        """Check if a node with the given value exists in the graph."""
        return value in self._adj_list

    @property
    def is_empty(self) -> bool:
        """Check if the graph contains no nodes."""
        return len(self) == 0

    # --- Modification Methods ---

    def add_node(self, value: T) -> None:
        """
        Add a new node to the graph if it does not already exist.

        Args:
            value: The value to be added as a node.
        """
        if value not in self._adj_list:
            self._adj_list[value] = Node(value)

    def add_edge(self, u: T, v: T, directed: bool = False) -> None:
        """
        Add an edge between two nodes. Nodes are created if they don't exist.

        Args:
            u: The value of the source node.
            v: The value of the destination node.
            directed: If True, the edge is one-way (u -> v).
                      Default is False (undirected).
        """
        self.add_node(u)
        self.add_node(v)

        node_u = self._adj_list[u]
        node_v = self._adj_list[v]

        node_u.neighbors.add(node_v)
        if not directed:
            node_v.neighbors.add(node_u)

    def remove_node(self, value: T) -> None:
        """
        Remove a node and all edges connected to it from the graph.

        Args:
            value: The value of the node to remove.
        """
        if value not in self._adj_list:
            return

        target_node = self._adj_list[value]

        # Optimized cleanup: only iterate over nodes that could have this neighbor
        for node in self._adj_list.values():
            node.neighbors.discard(target_node)

        del self._adj_list[value]

    def remove_edge(self, u: T, v: T, directed: bool = False) -> None:
        """
        Remove an edge between two nodes.

        Args:
            u: The value of the starting node.
            v: The value of the ending node.
            directed: If True, only remove the directed edge u -> v.
        """
        if u not in self._adj_list or v not in self._adj_list:
            return

        node_u = self._adj_list[u]
        node_v = self._adj_list[v]

        node_u.neighbors.discard(node_v)
        if not directed:
            node_v.neighbors.discard(node_u)

    # --- Access & Search Methods ---

    def get_neighbors(self, value: T) -> list[T]:
        """
        Return a list of values for all neighbors of a given node.

        Args:
            value: The node to get neighbors for.

        Returns:
            A list of values of the neighboring nodes.
        """
        if value not in self._adj_list:
            return []

        return [neighbor.value for neighbor in self._adj_list[value].neighbors]

    def has_edge(self, u: T, v: T) -> bool:
        """
        Check if there is an edge between two nodes.

        Args:
            u: The starting node value.
            v: The ending node value.

        Returns:
            True if the edge exists, False otherwise.
        """
        if u not in self._adj_list or v not in self._adj_list:
            return False

        return self._adj_list[v] in self._adj_list[u].neighbors

    # --- Traversal Methods ---

    def bfs(self, start_value: T) -> list[T]:
        """
        Perform a Breadth-First Search (BFS) starting from the given node.

        Args:
            start_value: The value of the node to start the traversal.

        Returns:
            A list of node values in BFS order.
        """
        if start_value not in self._adj_list:
            return []

        visited_order: list[T] = []
        visited: set[T] = {start_value}
        queue: Queue[Node[T]] = Queue()
        queue.enqueue(self._adj_list[start_value])

        while not queue.is_empty:
            current_node = queue.dequeue()
            visited_order.append(current_node.value)

            # Sort neighbors by value for deterministic traversal order
            for neighbor in sorted(current_node.neighbors, key=lambda x: x.value):
                if neighbor.value not in visited:
                    visited.add(neighbor.value)
                    queue.enqueue(neighbor)

        return visited_order

    def dfs(self, start_value: T) -> list[T]:
        """
        Perform a Depth-First Search (DFS) starting from the given node.

        Args:
            start_value: The value of the node to start the traversal.

        Returns:
            A list of node values in DFS order.
        """
        if start_value not in self._adj_list:
            return []

        visited_order: list[T] = []
        visited: set[T] = set()
        stack: Stack[Node[T]] = Stack()
        stack.push(self._adj_list[start_value])

        while not stack.is_empty:
            current_node = stack.pop()

            if current_node.value not in visited:
                visited.add(current_node.value)
                visited_order.append(current_node.value)

                # Reverse sort neighbors to maintain left-to-right order in stack
                sorted_neighbors = sorted(
                    current_node.neighbors, key=lambda x: x.value, reverse=True
                )

                for neighbor in sorted_neighbors:
                    if neighbor.value not in visited:
                        stack.push(neighbor)

        return visited_order
