"""
Leetcode
2265. Count Nodes Equal to Average of Subtree (medium)
2023-11-02

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

    The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    A subtree of root is a tree consisting of root and all of its descendants.

 

Example 1:

Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:

Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 1000
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
    Runtime: 39 ms, faster than 96.93% of Python3 online submissions for Count Nodes Equal to Average of Subtree.
    Memory Usage: 17.5 MB, less than 83.96% of Python3 online submissions for Count Nodes Equal to Average of Subtree.
    """

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal ans

            if not node:
                return (0, 0)

            left_cnt, left_sum = dfs(node.left)
            right_cnt, right_sum = dfs(node.right)

            cur_cnt = left_cnt + right_cnt + 1
            cur_sum = left_sum + right_sum + node.val

            if cur_sum // cur_cnt == node.val:
                ans += 1

            return (cur_cnt, cur_sum)

        dfs(root)

        return ans
