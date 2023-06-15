"""
Leetcode
1161. Maximum Level Sum of a Binary Tree (medium)
2023-06-15

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

from typing import List, Optional
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 315 ms, faster than 46.84% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
    Memory Usage: 21 MB, less than 67.41% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 1
        cur_level = 1
        max_sum = -inf

        q = [root]
        while q:
            cur_level_sum = 0
            next_level = []

            for _ in range(len(q)):
                node = q.pop(0)
                cur_level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if cur_level_sum > max_sum:
                max_sum = cur_level_sum
                ans = cur_level

            cur_level += 1
            q = next_level

        return ans


class Solution1:
    """
    leetcode solution: DFS
    Runtime: 329 ms, faster than 25.71% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
    Memory Usage: 21.1 MB, less than 24.67% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], level: int, level_sum: List) -> None:
            if not node:
                return

            if len(level_sum) == level:
                level_sum.append(node.val)
            else:
                level_sum[level] += node.val

            dfs(node.left, level + 1, level_sum)
            dfs(node.right, level + 1, level_sum)

        level_sum = []
        dfs(root, 0, level_sum)

        return 1 + level_sum.index(max(level_sum))
