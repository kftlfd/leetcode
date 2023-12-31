"""
Leetcode
101. Symmetric Tree (easy)
2023-03-13

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def fromString(cls, string):
        vals = string[1:-1].split(",")
        vals = map(lambda x: None if x == "null" else int(x), vals)
        return cls.build(list(vals))

    @classmethod
    def build(cls, values):
        if not values:
            return None

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
    wrong answer
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return

        def dfs(node):
            if not node:
                return [None]
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + [node.val] + dfs(node.right)

        vals = dfs(root)
        if len(vals) % 2 == 0:
            return False
        mid = len(vals) // 2
        return vals[:mid] == vals[mid+1:][::-1]


class Solution1:
    """
    Runtime: 40 ms, faster than 35.42% of Python3 online submissions for Symmetric Tree.
    Memory Usage: 14 MB, less than 52.37% of Python3 online submissions for Symmetric Tree.
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return

        if not root.left and not root.right:
            return True

        q_left = [root.left]
        q_right = [root.right]

        while q_left or q_right:
            vals_left = [node.val if node else None for node in q_left]
            vals_right = [node.val if node else None for node in q_right]
            if len(vals_left) != len(vals_right) or vals_left != vals_right[::-1]:
                return False

            new_left = []
            for node in q_left:
                if node:
                    new_left.append(node.left)
                    new_left.append(node.right)
            q_left = new_left

            new_right = []
            for node in q_right:
                if node:
                    new_right.append(node.left)
                    new_right.append(node.right)
            q_right = new_right

        return not q_left and not q_right


class Solution2:
    """
    https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python
    Runtime: 36 ms, faster than 61.30% of Python3 online submissions for Symmetric Tree.
    Memory Usage: 13.8 MB, less than 90.47% of Python3 online submissions for Symmetric Tree.
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        return False


s = Solution2()
tests = [
    ('[5,4,1,null,1,null,4,2,null,2,null]',
     False),

    ('[1,2,2,2,null,2]',
     False),

    ('[1,2,2,3,4,4,3]',
     True),

    ('[1,2,2,null,3,null,3]',
     False),
]
for inp, exp in tests:
    tree_root = TreeNode.fromString(inp)
    res = s.isSymmetric(tree_root)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
