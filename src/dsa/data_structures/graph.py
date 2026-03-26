from typing import Any, Protocol

from .queue import Queue
from .stack import Stack


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


class Node[T: Comparable]:
    """A graph node storing a value and a set of neighboring nodes."""

    value: T
    neighbors: set[Node[T]]

    def __init__(self, value: T) -> None:
        self.value = value
        self.neighbors = set()

    def __repr__(self) -> str:
        return f"Node({self.value})"


class Graph[T: Comparable]:
    """Adjacency list graph supporting directed and undirected edges, BFS and DFS."""

    _adj_list: dict[T, Node[T]]

    def __init__(self) -> None:
        self._adj_list = {}

    def __len__(self) -> int:
        return len(self._adj_list)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self._adj_list.keys())})"

    def __str__(self) -> str:
        lines = [
            f"{k} -> {sorted([n.value for n in node.neighbors])}"
            for k, node in self._adj_list.items()
        ]
        return "\n".join(lines)

    def __contains__(self, value: T) -> bool:
        return value in self._adj_list

    @property
    def is_empty(self) -> bool:
        return len(self) == 0

    def add_node(self, value: T) -> None:
        if value not in self._adj_list:
            self._adj_list[value] = Node(value)

    def add_edge(self, u: T, v: T, directed: bool = False) -> None:
        self.add_node(u)
        self.add_node(v)

        node_u = self._adj_list[u]
        node_v = self._adj_list[v]

        node_u.neighbors.add(node_v)
        if not directed:
            node_v.neighbors.add(node_u)

    def remove_node(self, value: T) -> None:
        if value not in self._adj_list:
            return

        target_node = self._adj_list[value]

        # Optimized cleanup: only iterate over nodes that could have this neighbor
        for node in self._adj_list.values():
            node.neighbors.discard(target_node)

        del self._adj_list[value]

    def remove_edge(self, u: T, v: T, directed: bool = False) -> None:
        if u not in self._adj_list or v not in self._adj_list:
            return

        node_u = self._adj_list[u]
        node_v = self._adj_list[v]

        node_u.neighbors.discard(node_v)
        if not directed:
            node_v.neighbors.discard(node_u)

    def get_neighbors(self, value: T) -> list[T]:
        if value not in self._adj_list:
            return []

        return [neighbor.value for neighbor in self._adj_list[value].neighbors]

    def has_edge(self, u: T, v: T) -> bool:
        if u not in self._adj_list or v not in self._adj_list:
            return False

        return self._adj_list[v] in self._adj_list[u].neighbors

    def bfs(self, start_value: T) -> list[T]:
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
