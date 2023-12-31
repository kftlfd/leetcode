"""
Leetcode
106. Construct Binary Tree from Inorder and Postorder Traversal (medium)
2023-03-16

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.toString()

    def toString(self):
        vals = []
        q = [self]
        while q:
            node = q.pop(0)
            if not node:
                vals.append('null')
                continue
            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        while vals[-1] == 'null':
            vals.pop()
        return f"[{','.join(vals)}]"


class Solution:
    """
    Runtime: 566 ms, faster than 5.04% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    Memory Usage: 90.3 MB, less than 6.78% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder or len(inorder) != len(postorder):
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        val = postorder[-1]

        in_sep = inorder.index(val)
        left_inorder = inorder[:in_sep]
        right_inorder = inorder[in_sep+1:]

        l = 0
        r = len(postorder) - 1
        while l < r:
            m = (l + r) // 2
            if postorder[m] in left_inorder:
                l = m + 1
            else:
                r = m
        post_sep = r

        left_postorder = postorder[:post_sep]
        right_postorder = postorder[post_sep:-1]

        left = self.buildTree(left_inorder, left_postorder)
        right = self.buildTree(right_inorder, right_postorder)
        return TreeNode(val, left, right)


class Solution1:
    """
    https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/A-better-Python-solution/759284
    Runtime: 43 ms, faster than 99.84% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    Memory Usage: 18.9 MB, less than 74.09% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        dict_inorder = {v: i for i, v in enumerate(inorder)}
        self.index = 1

        def build(idx_left, idx_right):
            if idx_left > idx_right:
                return None
            root = TreeNode(postorder[-self.index])
            self.index += 1
            idx_root = dict_inorder[root.val]
            root.right = build(idx_root+1, idx_right)
            root.left = build(idx_left, idx_root-1)
            return root

        return build(0, len(inorder)-1)


class Solution2:
    """
    https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/A-better-Python-solution
    Runtime: 140 ms, faster than 56.59% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    Memory Usage: 53.4 MB, less than 46.99% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)  # Line A

        root.right = self.buildTree(
            inorder[inorderIndex+1:], postorder)  # Line B
        root.left = self.buildTree(inorder[:inorderIndex], postorder)  # Line C

        return root


class Solution3:
    """
    https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/A-better-Python-solution
    Runtime: 47 ms, faster than 99.40% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    Memory Usage: 19 MB, less than 74.09% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)


s = Solution1()
tests = [
    (([1, 2, 3, 4], [2, 1, 4, 3]),
     '[3,1,4,null,2]'),

    (([1, 2], [2, 1]),
     '[1,null,2]'),

    (([2, 1], [2, 1]),
     '[1,2]'),

    (([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]),
     '[3,9,20,null,null,15,7]'),

    (([-1], [-1]),
     '[-1]')
]
for inp, exp in tests:
    res = s.buildTree(*inp).toString()
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
