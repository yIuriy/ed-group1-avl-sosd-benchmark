"""Skeleton for the augmented AVL tree used in the project."""

from __future__ import annotations


class Node:
    """Node used by the augmented AVL tree."""

    __slots__ = ("key", "left", "right", "height", "size", "sum")

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None
        self.height = 1
        self.size = 1
        self.sum = key


class AVLTree:
    """Augmented AVL tree skeleton for the Group 1 configuration."""

    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, key: int) -> None:
        """Insert a key into the AVL tree."""
        # TODO: Delegate to _insert and rebalance the tree.
        _ = key

    def delete(self, key: int) -> None:
        """Delete a key from the AVL tree if it exists."""
        # TODO: Delegate to _delete and rebalance the tree.
        _ = key

    def search(self, key: int) -> bool:
        """Return True when the key exists in the tree."""
        # TODO: Delegate to _search.
        _ = key
        return False

    def rank(self, key: int) -> int:
        """Return the number of keys less than or equal to the given key."""
        # TODO: Delegate to _rank.
        _ = key
        return 0

    def select(self, index: int) -> int | None:
        """Return the key at the given 0-based rank, if available."""
        # TODO: Delegate to _select.
        _ = index
        return None

    def range_sum(self, start: int, end: int) -> int:
        """Return the sum of keys in the inclusive interval [start, end]."""
        # TODO: Implement with prefix sums once the AVL is functional.
        _ = (start, end)
        return 0

    def _height(self, node: Node | None) -> int:
        """Return the cached height for a node."""
        # TODO: Return 0 for None and node.height otherwise.
        _ = node
        return 0

    def _size(self, node: Node | None) -> int:
        """Return the cached subtree size for a node."""
        # TODO: Return 0 for None and node.size otherwise.
        _ = node
        return 0

    def _subtree_sum(self, node: Node | None) -> int:
        """Return the cached subtree sum for a node."""
        # TODO: Return 0 for None and node.sum otherwise.
        _ = node
        return 0

    def _update(self, node: Node) -> None:
        """Refresh height, size, and sum after local modifications."""
        # TODO: Recompute metadata from children.
        _ = node

    def _balance_factor(self, node: Node | None) -> int:
        """Return the AVL balance factor for a node."""
        # TODO: Compute height(left) - height(right).
        _ = node
        return 0

    def _rotate_left(self, node: Node) -> Node:
        """Perform a left rotation and return the new subtree root."""
        # TODO: Implement AVL left rotation.
        return node

    def _rotate_right(self, node: Node) -> Node:
        """Perform a right rotation and return the new subtree root."""
        # TODO: Implement AVL right rotation.
        return node

    def _rebalance(self, node: Node) -> Node:
        """Restore AVL invariants after an update."""
        # TODO: Apply AVL rebalancing cases.
        return node

    def _insert(self, node: Node | None, key: int) -> Node:
        """Recursive insertion helper."""
        # TODO: Implement recursive insert with metadata updates.
        _ = (node, key)
        raise NotImplementedError("AVL insertion logic has not been implemented yet.")

    def _delete(self, node: Node | None, key: int) -> Node | None:
        """Recursive deletion helper."""
        # TODO: Implement recursive delete with metadata updates.
        _ = (node, key)
        raise NotImplementedError("AVL deletion logic has not been implemented yet.")

    def _search(self, node: Node | None, key: int) -> bool:
        """Recursive search helper."""
        # TODO: Implement recursive search.
        _ = (node, key)
        raise NotImplementedError("AVL search logic has not been implemented yet.")

    def _rank(self, node: Node | None, key: int) -> int:
        """Recursive rank helper."""
        # TODO: Implement rank using subtree sizes.
        _ = (node, key)
        raise NotImplementedError("AVL rank logic has not been implemented yet.")

    def _select(self, node: Node | None, index: int) -> int | None:
        """Recursive select helper."""
        # TODO: Implement select using subtree sizes.
        _ = (node, index)
        raise NotImplementedError("AVL select logic has not been implemented yet.")

    def _prefix_sum(self, node: Node | None, key: int) -> int:
        """Return the sum of keys less than or equal to the given key."""
        # TODO: Implement prefix sum using subtree sums.
        _ = (node, key)
        raise NotImplementedError("AVL prefix sum logic has not been implemented yet.")
