"""Skeleton for the unbalanced BST baseline used in comparisons."""

from __future__ import annotations


class BSTNode:
    """Simple node for the unbalanced BST baseline."""

    __slots__ = ("key", "left", "right")

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BSTree:
    """Unbalanced BST baseline skeleton."""

    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, key: int) -> None:
        """Insert a key into the baseline BST."""
        # TODO: Implement the unbalanced baseline insertion logic.
        _ = key

    def delete(self, key: int) -> None:
        """Delete a key from the baseline BST if it exists."""
        # TODO: Implement the unbalanced baseline deletion logic.
        _ = key

    def search(self, key: int) -> bool:
        """Return True when the key exists in the baseline BST."""
        # TODO: Implement the unbalanced baseline search logic.
        _ = key
        return False
