# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Binary Tree, 二叉树相关.
"""


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __getitem__(self, key):
        return self.left if key == 0 else self.right

    def __setitem__(self, key, value):
        if key == 0:
            self.left = value
        else:
            self.right = value

    def free(self):
        self.left = None
        self.right = None
        self.value = None


class DemoNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
