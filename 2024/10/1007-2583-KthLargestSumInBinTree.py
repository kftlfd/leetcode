"""
Leetcode
2024-10-22
2583. Kth Largest Sum in a Binary Tree
Medium

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:

Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.

Example 2:

Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.

 

Constraints:

    The number of nodes in the tree is n.
    2 <= n <= 10^5
    1 <= Node.val <= 10^6
    1 <= k <= n
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 49 ms, faster than 99.84% of Python3 online submissions for Kth Largest Sum in a Binary Tree.
    Memory Usage: 52.8 MB, less than 17.40% of Python3 online submissions for Kth Largest Sum in a Binary Tree.
    """

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        sums = []
        q = deque([root])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sums.append(level_sum)

        if len(sums) < k:
            return -1

        return sorted(sums)[-k]
