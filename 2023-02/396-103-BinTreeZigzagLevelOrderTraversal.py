"""
Leetcode
103. Binary Tree Zigzag Level Order Traversal (medium)
2023-02-19

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} ({self.left}, {self.right})"

    @classmethod
    def build(cls, values):
        if not values:
            return

        vals = values[:]
        root = cls(vals.pop(0))
        nodes = [root]

        while vals:
            node = nodes.pop(0)

            nextval = vals.pop(0)
            if nextval:
                node.left = cls(nextval)
                nodes.append(node.left)

            if not vals:
                break

            nextval = vals.pop(0)
            if nextval:
                node.right = cls(nextval)
                nodes.append(node.right)

        return root


class Solution:
    """
    Runtime: 39 ms, faster than 39.90% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    Memory Usage: 14.1 MB, less than 48.08% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    """

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        zigzag_levels = []
        q = [root]
        order = 0  # 0 = left-to-right, 1 = r-t-l

        while q:
            nxt_q = []
            curr_level = []
            for _ in range(len(q)):
                node = q.pop(0)

                if order == 0:
                    curr_level.append(node.val)
                else:
                    curr_level.insert(0, node.val)

                if node.left:
                    nxt_q.append(node.left)
                if node.right:
                    nxt_q.append(node.right)

            q = nxt_q
            zigzag_levels.append(curr_level)
            order = (order + 1) % 2  # flip 0 and 1

        return zigzag_levels


class Solution1:
    """
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/749036/Python-Clean-BFS-solution-explained
    Runtime: 38 ms, faster than 44.71% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    Memory Usage: 14 MB, less than 93.96% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
    """

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = [root]
        result = []
        direction = 1

        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level[::direction])
            direction *= (-1)

        return result


s = Solution1()
tests = [
    ([0, 2, 4, 1, None, 3, -1, 5, 1, None, 6, None, 8],
     [[0], [4, 2], [1, 3, -1], [8, 6, 1, 5]]),

    ([1, 2, 3, 4, None, None, 5],
     [[1], [3, 2], [4, 5]]),

    ([3, 9, 20, None, None, 15, 7],
     [[3], [20, 9], [15, 7]]),

    ([1],
     [[1]]),

    ([],
     [])
]
for inp, exp in tests:
    root = TreeNode.build(inp)
    res = s.zigzagLevelOrder(root)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
