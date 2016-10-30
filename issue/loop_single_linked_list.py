# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Loop Single Linked List.
"""


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


if __name__ == '__main__':

    def init_node_set():
        node_list = []
        for i in range(0, 10):
            _node = Node(i)
            if i == 0:
                node_list.append(_node)
            else:
                node_list[i - 1].next_node = _node
                node_list.append(_node)

        return node_list


    def init_node():
        node, node_cursor = None, None

        for i in range(0, 10):
            _node = Node(i)
            if not node_cursor:
                node = _node
            else:
                node_cursor.next_node = _node
            node_cursor = _node
        return node


    one = init_node_set()[0]
    # one = init_node()
    print('-' * 50)
    while one.next_node:
        print("Value: %s" % one.value)
        one = one.next_node

    print("None: %s" % one.value)
