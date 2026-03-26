import pytest

from dsa import BinarySearchTree

#  Tree Structure
#        50
#       /  \
#     30    70
#    /  \   /  \
#   20  40 60  80

TEST_DATA_INPUT = [50, 30, 20, 40, 70, 60, 80]

EXPECTED_INORDER = [20, 30, 40, 50, 60, 70, 80]  # Sorted
EXPECTED_PREORDER = [50, 30, 20, 40, 70, 60, 80]  # Root -> Left -> Right
EXPECTED_POSTORDER = [20, 40, 30, 60, 80, 70, 50]  # Left -> Right -> Root
EXPECTED_LEVEL_ORDER = [50, 30, 70, 20, 40, 60, 80]  # By levels

TREE_SIZE = 7
TREE_HEIGHT = 3


@pytest.fixture
def empty_tree():
    return BinarySearchTree()


@pytest.fixture
def populated_tree():
    bt = BinarySearchTree()
    for val in TEST_DATA_INPUT:
        bt.insert(val)
    return bt


def test_is_empty(empty_tree, populated_tree):
    assert empty_tree.is_empty
    assert not populated_tree.is_empty


def test_len(empty_tree, populated_tree):
    assert len(empty_tree) == 0
    assert len(populated_tree) == TREE_SIZE


def test_height(empty_tree, populated_tree):
    assert empty_tree.height() == 0
    assert populated_tree.height() == TREE_HEIGHT


def test_search_found(populated_tree):
    assert populated_tree.search(50)
    assert populated_tree.search(20)
    assert populated_tree.search(40)
    assert populated_tree.search(80)


def test_search_not_found(populated_tree, empty_tree):
    assert not populated_tree.search(999)
    assert not populated_tree.search(0)
    assert not empty_tree.search(50)


def test_insert_duplicates(populated_tree):
    populated_tree.insert(50)
    populated_tree.insert(20)
    assert len(populated_tree) == TREE_SIZE


def test_insert_single(empty_tree):
    empty_tree.insert(10)
    assert not empty_tree.is_empty
    assert empty_tree.height() == 1
    assert empty_tree.search(10)


def test_inorder_traversal(populated_tree, empty_tree):
    assert populated_tree.inorder() == EXPECTED_INORDER
    assert empty_tree.inorder() == []


def test_preorder_traversal(populated_tree, empty_tree):
    assert populated_tree.preorder() == EXPECTED_PREORDER
    assert empty_tree.preorder() == []


def test_postorder_traversal(populated_tree, empty_tree):
    assert populated_tree.postorder() == EXPECTED_POSTORDER
    assert empty_tree.postorder() == []


def test_bfs_traversal(populated_tree, empty_tree):
    assert populated_tree.bfs() == EXPECTED_LEVEL_ORDER
    assert empty_tree.bfs() == []
