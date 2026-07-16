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
        if self.root is None:
            self.root = BSTNode(key)
            return

        current = self.root

        while True:
            if key == current.key:
                return

            elif key < current.key:
                if current.left is None:
                    current.left = BSTNode(key)
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = BSTNode(key)
                    return
                current = current.right

    def delete(self, key: int) -> None:
        """Delete a key from the baseline BST if it exists."""
        current = self.root
        parent = None

        while current is not None and current.key != key:
            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left is current:
                parent.left = None
            else:
                parent.right = None
            return
        
        if current.left is None or current.right is None:
            if current.left is not None:
                child = current.left
            else:
                child = current.right

            if parent is None:
                self.root = child
            elif parent.left is current:
                parent.left = child
            else:
                parent.right = child
            return
        
        successor_parent = current
        successor = current.right

        while successor.left is not None:
            successor_parent = successor
            successor = successor.left

        current.key = successor.key

        if successor_parent.left is successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

    def search(self, key: int) -> bool:
        """Return True when the key exists in the baseline BST."""
        current = self.root

        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
                
        return False
