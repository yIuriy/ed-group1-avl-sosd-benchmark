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
        self.root = self._insert(self.root, key)

    def delete(self, key: int) -> None:
        """Delete a key from the AVL tree if it exists."""
        self.root = self._delete(self.root, key)

    def search(self, key: int) -> bool:
        """Return True when the key exists in the tree."""
        return self._search(self.root, key)
        
    def rank(self, key: int) -> int:
        """Return the number of keys less than or equal to the given key."""
        return self._rank(self.root, key)

    def select(self, index: int) -> int | None:
        """Return the key at the given 0-based rank, if available."""
        if self.root is None or index < 0 or index >= self._size(self.root):
            return None
        return self._select(self.root, index)

    def range_sum(self, start: int, end: int) -> int:
        """Return the sum of keys in the inclusive interval [start, end]."""
        if start > end:
            return 0
        return self._prefix_sum(self.root, end) - self._prefix_sum(self.root, start -1)

    def _height(self, node: Node | None) -> int:
        """Return the cached height for a node."""
        if node is None:
            return 0
        return node.height

    def _size(self, node: Node | None) -> int:
        """Return the cached subtree size for a node."""
        if node is None:
            return 0
        return node.size
        
    def _subtree_sum(self, node: Node | None) -> int:
        """Return the cached subtree sum for a node."""
        if node is None: 
            return 0
        return node.sum 

    def _update(self, node: Node) -> None:
        """Refresh height, size, and sum after local modifications."""
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node.size = 1 + self._size(node.left) + self._size(node.right)
        node.sum = node.key + self._subtree_sum(node.left) + self._subtree_sum(node.right)
        
    def _balance_factor(self, node: Node | None) -> int:
        """Return the AVL balance factor for a node."""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, node: Node) -> Node:
        """Perform a left rotation and return the new subtree root."""
        y = node.right
        t2 = y.left
        
        y.left = node
        node.right = t2
        
        self._update(node)
        self._update(y)
        
        return y
 
    def _rotate_right(self, node: Node) -> Node:
        """Perform a right rotation and return the new subtree root."""
        x = node.left 
        t2 = x.right  
        
        x.right = node
        node.left = t2
        
        self._update(node)
        self._update(x)
        
        return x
    
    def _rebalance(self, node: Node) -> Node:
        """Restore AVL invariants after an update."""
        self._update(node)
        factor = self._balance_factor(node)
        
        if factor > 1: # left heavy 
            if self._balance_factor(node.left) < 0:
               node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        elif factor < -1:
            if self._balance_factor(node.right) > 0:
               node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _insert(self, node: Node | None, key: int) -> Node:
        """Recursive insertion helper."""
        if node is None:
            return Node(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node 
        
        return self._rebalance(node)

    def _delete(self, node: Node | None, key: int) -> Node | None:
        """Recursive deletion helper."""
        if node is None:
            return None
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.right
                
                while successor.left is not None:
                    successor = successor.left
                                        
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)
                
        return self._rebalance(node)
        
    def _search(self, node: Node | None, key: int) -> bool:
        """Recursive search helper."""
        if node is None:
            return False
        
        if key == node.key:
            return True
        
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _rank(self, node: Node | None, key: int) -> int:
        """Recursive rank helper."""
        if node is None:
            return 0
        
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return self._size(node.left) + 1 + self._rank(node.right, key)
        else:
            return self._size(node.left) + 1
        
    def _select(self, node: Node | None, index: int) -> int | None:
        """Recursive select helper."""        
        left_size = self._size(node.left)
        
        if index < left_size:
            return self._select(node.left, index)
        elif index == left_size:
            return node.key
        else:
            return self._select(node.right, index - left_size - 1)
            
    def _prefix_sum(self, node: Node | None, key: int) -> int:
        """Return the sum of keys less than or equal to the given key."""
        if node is None:
            return 0
        
        if key < node.key:
            return self._prefix_sum(node.left, key)
        else:
            return self._subtree_sum(node.left) + node.key + self._prefix_sum(node.right, key)