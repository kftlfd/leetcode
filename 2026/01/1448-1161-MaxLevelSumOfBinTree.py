"""
Leetcode
2026-01-06
1161. Maximum Level Sum of a Binary Tree
Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5


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
    Runtime 11ms Beats 94.02%
    Memory 23.03MB Beats 13.07%
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = -9999999
        max_sum_level = 0
        cur_level = 0
        q = [root]

        while q:
            cur_level += 1
            cur_sum = 0
            nxt_q = []
            for node in q:
                cur_sum += node.val
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_sum_level = cur_level
            q = nxt_q

        return max_sum_level
