#!/usr/bin/env python3

import math
from random import randint

from binary_tree import Node, traverse_iter, traverse_recur


def build_tree_recur(lst: list) -> Node or None:
    """build a binary tree from a list"""
    if not lst:
        return None

    node = Node(lst[0])
    mid = len(lst) // 2 + 1
    node.left = build_tree_recur(lst[1:mid])
    node.right = build_tree_recur(lst[mid:])

    return node


def build_tree_iter(lst: list) -> Node or None:
    """build a binary tree from a list"""
    if not lst:
        return None

    root = Node(lst[0])
    queue = [root]

    for i in range(1, len(lst), 2):
        node = queue.pop(0)
        node.left = Node(lst[i])
        queue.append(node.left)
        if i + 1 < len(lst):
            node.right = Node(lst[i + 1])
            queue.append(node.right)

    return root


def tree_sum_recur(root: Node) -> int:
    """sum all the values in a binary tree recursively"""
    if root is None:
        return 0

    return root.value + tree_sum_recur(root.left) + tree_sum_recur(root.right)


def tree_sum_iter(root: Node) -> int:
    """sum all the values in a binary tree iteratively"""
    if root is None:
        return 0

    queue = [root]
    total = 0

    while queue:
        node = queue.pop()
        total += node.value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return total


def tree_min_recur(root: Node) -> int:
    """find the minimum value in a binary tree"""
    if root is None:
        return math.inf

    min_left = tree_min_recur(root.left)
    min_right = tree_min_recur(root.right)

    return min(root.value, min_left, min_right)


def tree_max_recur(root: Node) -> int:
    """find the maximum value in a binary tree"""
    if root is None:
        return -math.inf

    max_left = tree_max_recur(root.left)
    max_right = tree_max_recur(root.right)

    return max(root.value, max_left, max_right)


def tree_min_iter(root: Node) -> int:
    """find the minimum value in a binary tree"""
    if root is None:
        return math.inf

    queue = [root]
    min_val = root.value

    while queue:
        node = queue.pop(0)
        min_val = min(min_val, node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return min_val


def tree_max_iter(root: Node) -> int:
    """find the maximum value in a binary tree"""
    if root is None:
        return -math.inf

    queue = [root]
    max_val = root.value

    while queue:
        node = queue.pop(0)
        max_val = max(max_val, node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return max_val


def tree_height_recur(root: Node) -> int:
    """find the height of a binary tree"""
    if root is None:
        return 0

    return 1 + max(tree_height_recur(root.left), tree_height_recur(root.right))


def tree_height_iter(root: Node) -> int:
    """find the height of a binary tree"""
    if root is None:
        return 0

    queue = [root]
    height = 0

    while queue:
        height += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return height


def tree_search_recur(root: Node, value: int) -> bool:
    """search a binary tree for a value recursively and return True if found"""
    if root is None:
        return False

    if root.value == value:
        return True

    return tree_search_recur(root.left, value) or tree_search_recur(root.right, value)


def tree_search_iter(root: Node, value: int) -> bool:
    """search a binary tree for a value iteratively and return True if found"""
    if root is None:
        return False

    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.value == value:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False


def tree_max_path_sum(root: Node) -> int:
    """find the maximum path sum in a binary tree"""
    if root is None:
        return 0

    max_left = tree_max_path_sum(root.left)
    max_right = tree_max_path_sum(root.right)

    return max(max_left, max_right) + root.value


def tree_leaf_mean(root: Node) -> float:
    """find the mean of all the leaf nodes in a binary tree"""
    if root is None:
        return 0

    queue = [root]
    total = 0
    count = 0

    while queue:
        node = queue.pop(0)
        if node.left is None and node.right is None:
            total += node.value
            count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return total / count


def main():
    lst = [randint(-10, 10) for _ in range(10)]
    print(lst)
    root = build_tree_recur(lst)

    print("traverse_recur: ", traverse_recur(root))
    print("traverse_iter: ", traverse_iter(root))

    print("tree_sum_recur: ", tree_sum_recur(root))
    print("tree_sum_iter: ", tree_sum_iter(root))

    print("tree_min_recur: ", tree_min_recur(root))
    print("tree_min_iter: ", tree_min_iter(root))

    print("tree_height_recur: ", tree_height_recur(root))
    print("tree_height_iter: ", tree_height_iter(root))

    print("tree_max_path_sum_recur: ", tree_max_path_sum(root))
    print("tree_level_mean: ", tree_leaf_mean(root))


if __name__ == "__main__":
    main()
