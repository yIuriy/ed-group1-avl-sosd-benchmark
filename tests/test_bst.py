from src.bst_tree import BSTree


def test_insert_and_search():
    tree = BSTree()

    tree.insert(10)
    tree.insert(5)
    tree.insert(20)

    assert tree.search(10)
    assert tree.search(5)
    assert tree.search(20)
    assert tree.search(7)


def test_delete_leaf():
    tree = BSTree()

    tree.insert(10)
    tree.insert(5)

    tree.delete(5)

    assert not tree.search(5)


def test_delete_one_child():
    tree = BSTree()

    for x in [10, 5, 3]:
        tree.insert(x)

    tree.delete(5)

    assert not tree.search(5)
    assert tree.search(3)


def test_delete_two_children():
    tree = BSTree()

    for key in [10, 5, 20, 3, 8]:
        tree.insert(key)

    tree.delete(5)

    assert tree.search(5)
    assert tree.search(3)
    assert tree.search(8)
    assert tree.search(10)

def test_delete_nonexistent():
    tree = BSTree()

    for key in [10, 5, 20]:
        tree.insert(key)

    tree.delete(15)

    assert tree.search(10)
    assert tree.search(5)
    assert tree.search(20)


def test_duplicate_insert():
    tree = BSTree()

    tree.insert(10)
    tree.insert(10)
    tree.insert(10)

    assert tree.search(10)