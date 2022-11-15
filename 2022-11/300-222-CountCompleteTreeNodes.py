"""
Leetcode
222. Count Complete Tree Nodes (medium)
2022-11-15

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 75 ms, faster than 97.78% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.4 MB, less than 46.74% of Python3 online submissions for Count Complete Tree Nodes.
class Solution:
    def findHeight(self, root: TreeNode) -> int:
        """get height/depth of tree"""
        h = 0
        curr = root
        while curr.left:
            h += 1
            curr = curr.left
        return h

    def getNode(self, root, height, index) -> TreeNode:
        """returns node at index of row of tree at given height. """
        if height == 0:
            return root

        curr = root
        path = format(index, f'0{height}b')  # 0=left, 1=right
        for move in path:
            if move == "0":
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        h = self.findHeight(root)

        lastRowMaxWidth = 2 ** h

        # binary search for the last node in last tree row
        l = 0
        r = lastRowMaxWidth - 1
        while l <= r:
            m = (l + r) // 2
            node = self.getNode(root, h, m)
            if node:
                l = m + 1
            else:
                r = m - 1

        lastRowNodeCount = l

        return sum(2 ** e for e in range(h)) + lastRowNodeCount


# https://leetcode.com/problems/count-complete-tree-nodes/discuss/701466/Python-O(log-n-*-log-n)-solution-with-Binary-Search-explained
# Runtime: 148 ms, faster than 69.82% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.6 MB, less than 11.61% of Python3 online submissions for Count Complete Tree Nodes.
class Solution1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # find tree height
        h, curr = 0, root
        while curr.left:
            h, curr = h+1, curr.left

        if h == 0:
            return 1

        def isNode(index: int) -> bool:
            path = bin(index)[3:]  # skip the '0b' and first digit
            curr = root
            for move in path:
                if move == "0":
                    curr = curr.left
                else:
                    curr = curr.right
            return curr != None

        # binary search
        l = 1 << h  # same as 2**h -- index of first node in the last row
        r = (1 << (h+1)) - 1  # -- last node in the last row

        # special case, if tree is perfect (last row is complete)
        if isNode(r):
            return r

        while l <= r:
            m = (l + r) // 2
            if isNode(m):
                l = m + 1
            else:
                r = m - 1

        return r


# Runtime: 199 ms, faster than 28.82% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.5 MB, less than 46.74% of Python3 online submissions for Count Complete Tree Nodes.
class Solution2:
    def findHeight(self, root: TreeNode) -> int:
        """get height/depth of tree"""
        h, curr = 0, root
        while curr.left:
            h, curr = h+1, curr.left
        return h

    def getNode(self, root, height, index) -> TreeNode:
        """returns node at index of row of tree at given height. """
        curr = root
        path = format(index, f'b')[1:]  # 0=left, 1=right
        for move in path:
            if move == "0":
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        h = self.findHeight(root)
        if h == 0:
            return 1

        # binary search for the last node in last tree row
        first = 2 ** h
        last = (2 ** (h+1)) - 1
        while first <= last:
            m = (first + last) // 2
            node = self.getNode(root, h, m)
            if node:
                first = m + 1
            else:
                last = m - 1

        return last


# https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
# Runtime: 68 ms, faster than 99.64% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.5 MB, less than 46.74% of Python3 online submissions for Count Complete Tree Nodes.
class Solution3:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)


def createTree(vals: Optional[list]) -> Optional[TreeNode]:
    if not vals:
        return
    vals = vals[:]
    root = TreeNode(vals.pop(0))
    q = [root]
    while q:
        node = q.pop(0)

        if not vals:
            break
        node.left = TreeNode(vals.pop(0))

        if not vals:
            break
        node.right = TreeNode(vals.pop(0))

        q.append(node.left)
        q.append(node.right)
    return root


s = Solution2()
tests = [
    ([1, 2, 3, 4, 5, 6],
     6),

    ([],
     0),

    ([1],
     1),
]
for inp, exp in tests:
    root = createTree(inp)
    res = s.countNodes(root)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
