# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

from binarytree import tree, Node

"""
Binary Tree, 二叉树相关.
"""


def build_node():
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


def horizontal_data(tree_node):
    """横向输出二叉树节点数据.

    如下二叉树示图:

          ___13________
         /             \
        8            ___2__
       / \          /      \
      7   14      _4        5
     /           /  \      /
    0           12   11   9


    输出: [13,8,2,7,14,4,5,0,12,11,9]
    """

    info_list = []
    node_list = [tree_node]

    def check_empty(node):
        if node:
            node_list.append(node)

    while node_list:
        current_node = node_list.pop(0)
        info_list.append(current_node.value)

        check_empty(current_node.left)
        check_empty(current_node.right)

    return info_list


def horizontal_data2(tree_node):
    """其实是个队列, python里没有原生, 使用标准库里形式实现, 此方案不推荐, 性能比较可见 measure().
    """
    info_list = []
    node_list = Queue()
    node_list.put(tree_node)

    def check_empty(node):
        if node:
            node_list.put(node)

    while not node_list.empty():
        current_node = node_list.get()
        info_list.append(current_node.value)

        check_empty(current_node.left)
        check_empty(current_node.right)

    return info_list


def test():
    demo_data = tree()

    print(demo_data)
    # print(demo_data.values)
    # print(demo_data.properties)

    print(horizontal_data(demo_data))


def measure():
    from timeit import repeat, default_timer

    print(repeat("horizontal_data(demo)", "from __main__ import horizontal_data,demo", default_timer, 10, 10000))
    print(repeat("horizontal_data2(demo)", "from __main__ import horizontal_data2,demo", default_timer, 10, 10000))


if __name__ == "__main__":
    # demo = build_node()
    # print(demo)
    # measure()

    test()
