"""
Leetcode
129. Sum Root to Leaf Numbers
Medium
2024-04-15

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 39 ms, faster than 29.64% of Python3 online submissions for Sum Root to Leaf Numbers.
    Memory Usage: 16.4 MB, less than 81.07% of Python3 online submissions for Sum Root to Leaf Numbers.
    """

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], cur_num):
            nonlocal ans

            if not node:
                return

            cur_num = cur_num * 10 + node.val

            if not node.left and not node.right:
                ans += cur_num

            dfs(node.left, cur_num)
            dfs(node.right, cur_num)

        dfs(root, 0)

        return ans
