"""
Leetcode
1372. Longest ZigZag Path in a Binary Tree (medium)
2023-04-19

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

    Choose any node in the binary tree and a direction (right or left).
    If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
    Change the direction from right to left or from left to right.
    Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    Time Limit Exceeded. 52 / 58 test cases passed.
    """

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT = 0
        RIGHT = 1

        def maxZigZag(node: Optional[TreeNode], direction: int) -> int:
            if not node or (not node.left and not node.right):
                return 0

            if direction == LEFT:
                if not node.left:
                    return 0
                return maxZigZag(node.left, RIGHT) + 1

            if direction == RIGHT:
                if not node.right:
                    return 0
                return maxZigZag(node.right, LEFT) + 1

        def traverse(node: Optional[TreeNode]):
            if not node:
                return []
            return traverse(node.left) + [maxZigZag(node, LEFT), maxZigZag(node, RIGHT)] + traverse(node.right)

        return max(traverse(root))


class Solution2:
    """
    leetcode solution
    Runtime: 494 ms, faster than 31.87% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
    Memory Usage: 61.8 MB, less than 28.94% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
    """

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        path_len = 0
        LEFT = 0
        RIGHT = 1

        def maxZigZag(node: Optional[TreeNode], direction: int, steps: int) -> int:
            nonlocal path_len

            if node:
                path_len = max(path_len, steps)
                if direction == LEFT:
                    maxZigZag(node.left, RIGHT, steps + 1)
                    maxZigZag(node.right, LEFT, 1)
                else:
                    maxZigZag(node.left, RIGHT, 1)
                    maxZigZag(node.right, LEFT, steps + 1)

        maxZigZag(root, LEFT, 0)
        maxZigZag(root, RIGHT, 0)

        return path_len
