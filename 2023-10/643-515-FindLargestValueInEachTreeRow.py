"""
Leetcode
515. Find Largest Value in Each Tree Row (medium)
2023-10-24

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
    Runtime: 49 ms, faster than 65.94% of Python3 online submissions for Find Largest Value in Each Tree Row.
    Memory Usage: 18.6 MB, less than 70.35% of Python3 online submissions for Find Largest Value in Each Tree Row.
    """

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return ans

        q = [root]
        while q:
            row_max = -float('inf')
            nxt_q = []
            for node in q:
                row_max = max(row_max, node.val)
                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)
            ans.append(row_max)
            q = nxt_q

        return ans


class Solution1:
    """
    leetcode solution 2: dfs
    Runtime: 47 ms, faster than 75.34% of Python3 online submissions for Find Largest Value in Each Tree Row.
    Memory Usage: 19.5 MB, less than 9.40% of Python3 online submissions for Find Largest Value in Each Tree Row.
    """

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return ans


class Solution2:
    """
    leetcode solution 3: dfs iterative
    Runtime: 56 ms, faster than 19.20% of Python3 online submissions for Find Largest Value in Each Tree Row.
    Memory Usage: 18.5 MB, less than 99.06% of Python3 online submissions for Find Largest Value in Each Tree Row.
    """

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()
            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans
