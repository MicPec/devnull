#!/usr/bin/env python3
import math
from random import randint
from binary_tree import Node, traverse_recur, traverse_iter
import binary_tree_algorithms as bta

import unittest


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        # self.lst = [i for i in range(0, 20)]
        self.lst = [randint(-100, 100) for _ in range(20)]
        self.root = bta.build_tree_iter(self.lst)

    def test_build_tree_recur(self):
        lst = list(range(10))
        root = bta.build_tree_recur(lst)
        self.assertEqual(traverse_recur(root), lst)

    def test_build_tree_iter(self):
        lst = list(range(10))
        root = bta.build_tree_iter(lst)
        self.assertEqual(traverse_iter(root), lst)

    def test_sum_tree(self):
        self.assertEqual(bta.sum_tree_recur(self.root), sum(self.lst))
        self.assertEqual(bta.sum_tree_iter(self.root), sum(self.lst))

    def test_sum_tree_empty(self):
        self.assertEqual(bta.sum_tree_recur(None), 0)
        self.assertEqual(bta.sum_tree_iter(None), 0)

    def test_tree_min(self):
        self.assertEqual(bta.tree_min_recur(self.root), min(self.lst))
        self.assertEqual(bta.tree_min_iter(self.root), min(self.lst))

    def test_tree_min_empty(self):
        self.assertEqual(bta.tree_min_recur(None), math.inf)
        self.assertEqual(bta.tree_min_iter(None), math.inf)

    def test_tree_max(self):
        self.assertEqual(bta.tree_max_recur(self.root), max(self.lst))
        self.assertEqual(bta.tree_max_iter(self.root), max(self.lst))

    def test_tree_max_empty(self):
        self.assertEqual(bta.tree_max_recur(None), -math.inf)
        self.assertEqual(bta.tree_max_iter(None), -math.inf)

    def test_tree_height(self):
        self.assertEqual(bta.tree_height_recur(self.root), 5)
        self.assertEqual(bta.tree_height_iter(self.root), 5)

    def test_tree_height_empty(self):
        self.assertEqual(bta.tree_height_recur(None), 0)
        self.assertEqual(bta.tree_height_iter(None), 0)

    def test_search_tree_recur(self):
        self.assertTrue(bta.tree_search_recur(self.root, self.lst[0]))
        self.assertFalse(bta.tree_search_recur(self.root, 1000))

    def test_search_tree_iter(self):
        self.assertTrue(bta.tree_search_iter(self.root, self.lst[0]))
        self.assertFalse(bta.tree_search_iter(self.root, 1000))

    def test_tree_max_path_sum(self):
        lst = list(range(10))
        root = bta.build_tree_recur(lst)
        self.assertEqual(bta.tree_max_path_sum(root), 21)

    def test_tree_max_path_sum_empty(self):
        self.assertEqual(bta.tree_max_path_sum(None), 0)

    def test_tree_leaf_mean(self):
        lst = list(range(1, 6))
        root = bta.build_tree_recur(lst)
        self.assertEqual(bta.tree_leaf_mean(root), 4)
