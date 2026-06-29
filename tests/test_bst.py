from src.bst_tree import BSTree
from src.avl_tree import AVLTree


TREE_CLASSES = [BSTree, AVLTree]


def test_insert_and_search():
    for TreeClass in TREE_CLASSES:
        tree = TreeClass()

        tree.insert(10)
        tree.insert(5)
        tree.insert(20)

        assert tree.search(10)
        assert tree.search(5)
        assert tree.search(20)
        assert not tree.search(7)


def test_delete_leaf():
    for TreeClass in TREE_CLASSES:
        tree = TreeClass()

        tree.insert(10)
        tree.insert(5)

        tree.delete(5)

        assert not tree.search(5)


def test_delete_one_child():
    for TreeClass in TREE_CLASSES:
        tree = TreeClass()

        for x in [10, 5, 3]:
            tree.insert(x)

        tree.delete(5)

        assert not tree.search(5)
        assert tree.search(3)


def test_delete_two_children():
    for TreeClass in TREE_CLASSES:
        tree = TreeClass()

        for key in [10, 5, 20, 3, 8]:
            tree.insert(key)

        tree.delete(5)

        assert not tree.search(5)
        assert tree.search(3)
        assert tree.search(8)
        assert tree.search(10)


def test_delete_nonexistent():
    for TreeClass in TREE_CLASSES:
        tree = TreeClass()

        for key in [10, 5, 20]:
            tree.insert(key)

        tree.delete(15)

        assert tree.search(10)
        assert tree.search(5)
        assert tree.search(20)


def test_duplicate_insert():
    for TreeClass in TREE_CLASSES:
        tree = TreeClass()

        tree.insert(10)
        tree.insert(10)
        tree.insert(10)

        assert tree.search(10)