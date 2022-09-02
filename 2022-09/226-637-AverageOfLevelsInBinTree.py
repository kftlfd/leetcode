"""
Leetcode
637. Average of Levels in Binary Tree (easy)
2022-09-02

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 88 ms, faster than 36.89% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.5 MB, less than 46.07% of Python3 online submissions for Average of Levels in Binary Tree.
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        ans = []
        while q:
            level_vals = []
            q2 = []
            for node in q:
                level_vals.append(node.val)
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            ans.append(sum(level_vals) / len(level_vals))
            q = q2
        return ans


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
