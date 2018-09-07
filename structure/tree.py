# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

try:
    from node import TreeNode, DemoNode as Node
    from binary_tree import horizontal_data
except ImportError:
    from .node import TreeNode, DemoNode as Node
    from .binary_tree import horizontal_data

"""
Binary Tree, 二叉树相关.
"""


def build_data():
    """构建出如下树结构:

             ____11_____
            /           \
         __8__        ___0
        /     \      /    \
      _1       7    6      2
     /  \     /      \      \
    12   9   4        13     10
    """
    # 0
    root = Node(11)

    # 1
    root.left = Node(8)
    root.right = Node(0)

    # 2
    root.left.left = Node(1)
    root.left.right = Node(7)

    root.right.left = Node(6)
    root.right.right = Node(2)

    # 3
    root.left.left.left = Node(12)
    root.left.left.right = Node(9)

    root.left.right.left = Node(4)

    root.right.left.right = Node(13)
    root.right.right.right = Node(10)

    return root


def build_data2():
    """构建出如下树结构:

             ____11_____
            /           \
         __8__        ___0
        /     \      /    \
      _1       7    6      2
     /  \     /      \      \
    12   9   4        13     10
    """
    # 0
    root = TreeNode(11)

    # 1
    root[0] = TreeNode(8)
    root[1] = TreeNode(0)

    # 2
    root[0][0] = TreeNode(1)
    root[0][1] = TreeNode(7)

    root[1][0] = TreeNode(6)
    root[1][1] = TreeNode(2)

    # 3
    root[0][0][0] = TreeNode(12)
    root[0][0][1] = TreeNode(9)

    root[0][1][0] = TreeNode(4)

    root[1][0][1] = TreeNode(13)
    root[1][1][1] = TreeNode(10)

    return root


def test():
    demo = build_data()
    print(demo)
    print(horizontal_data(demo))


def test2():
    demo = build_data2()
    print(demo)
    print(horizontal_data(demo))


if __name__ == "__main__":
    test()
    test2()
