#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return f"Node({self.value}, L:{self.left}, R:{self.right})"


def init_tree() -> Node:
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    c.right = f

    d.left = g
    d.right = h

    return a


def traverse_recur(node):
    """depth-first traversal"""
    if node is None:
        return []

    left = traverse_recur(node.left)
    right = traverse_recur(node.right)

    return [node.value] + left + right


def traverse_iter(node):
    """breadth-first traversal"""
    if node is None:
        return []

    queue = [node]
    vals = []

    while queue:
        node = queue.pop(0)
        vals.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return vals


def main():
    tree = init_tree()
    tree_vals_recur = traverse_recur(tree)
    print("traverse_recur: ", tree_vals_recur)
    tree_vals_iter = traverse_iter(tree)
    print("traverse_iter: ", tree_vals_iter)


if __name__ == "__main__":
    main()
