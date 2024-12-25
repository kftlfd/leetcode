"""
Leetcode
2024-12-25
515. Find Largest Value in Each Tree Row
Medium

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:

Input: root = [1,2,3]
Output: [1,3]

 

Constraints:

    The number of nodes in the tree will be in the range [0, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Largest Value in Each Tree Row.
    Memory Usage: 19.8 MB, less than 6.38% of Python3 online submissions for Find Largest Value in Each Tree Row.
    """

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = [root]
        while q:
            ans.append(max(node.val for node in q))
            nxt_q = []
            for node in q:
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            q = nxt_q

        return ans
