from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

#O(n)|O(d)
def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    return helper(tree, [])

def helper(node, array):
    if node:
        helper(node.left, array)
        array.append(node.data)
        helper(node.right, array)
    return array


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
