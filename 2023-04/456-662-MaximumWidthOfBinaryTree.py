"""
Leetcode
662. Maximum Width of Binary Tree (medium)
2023-04-20

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """
    Time Limit Exceeded. 94 / 114 test cases passed.
    """

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_width = 0

        def trimQ(arr):
            start = 0
            while start < len(arr) and arr[start] is None:
                start += 1
            end = len(arr) - 1
            while end >= 0 and arr[end] is None:
                end -= 1
            return arr[start:end+1]

        q = [root]
        while q:
            max_width = max(max_width, len(q))
            next_q = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    next_q.append(node.left)
                    next_q.append(node.right)
                else:
                    next_q.append(None)
                    next_q.append(None)
            q = trimQ(next_q)

        return max_width


class Solution2:
    """
    https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/1803613/Python-3-BFS-and-DFS-Solutions-and-Explanation
    Runtime: 45 ms, faster than 72.26% of Python3 online submissions for Maximum Width of Binary Tree.
    Memory Usage: 14.8 MB, less than 39.48% of Python3 online submissions for Maximum Width of Binary Tree.
    """

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Each index in queue store node and its index in its level
        queue = [(root, 0)]
        maxLength = 1
        while queue:
            nextLevelQueue = []
            # Calculate leftMost and rightMost node
            leftMost, rightMost = queue[0][1], queue[-1][1]
            maxLength = max(maxLength, rightMost - leftMost + 1)

            # Append next level's node into new queue
            for currNode, idx in queue:
                # If left, right child exist: append it and its idx
                if currNode.left:
                    nextLevelQueue.append((currNode.left, idx * 2))
                if currNode.right:
                    nextLevelQueue.append((currNode.right, idx * 2 + 1))
            # Replace queue to nextLevelQueue
            queue = nextLevelQueue
        return maxLength
