"""
Leetcode
1382. Balance a Binary Search Tree
Medium
2024-06-26

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

 

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    1 <= Node.val <= 105
"""


# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 198 ms, faster than 64.92% of Python3 online submissions for Balance a Binary Search Tree.
    Memory Usage: 22 MB, less than 60.27% of Python3 online submissions for Balance a Binary Search Tree.
    """

    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        dfs(root)

        def build_tree(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = TreeNode(vals[mid])
            node.left = build_tree(start, mid - 1)
            node.right = build_tree(mid + 1, end)
            return node

        return build_tree(0, len(vals) - 1)


class Solution2:
    """
    leetcode solution 2: Day-Stout-Warren Algorithm / In-Place Balancing
    Runtime: 265 ms, faster than 5.17% of Python3 online submissions for Balance a Binary Search Tree.
    Memory Usage: 20.5 MB, less than 80.50% of Python3 online submissions for Balance a Binary Search Tree.
    """

    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # Step 1: Create the backbone (vine)
        # Temporary dummy node
        vine_head = TreeNode(0)
        vine_head.right = root
        current = vine_head
        while current.right:
            if current.right.left:
                self.right_rotate(current, current.right)
            else:
                current = current.right

        # Step 2: Count the nodes
        node_count = 0
        current = vine_head.right
        while current:
            node_count += 1
            current = current.right

        # Step 3: Create a balanced BST
        m = 2 ** math.floor(math.log2(node_count + 1)) - 1
        self.make_rotations(vine_head, node_count - m)
        while m > 1:
            m //= 2
            self.make_rotations(vine_head, m)

        balanced_root = vine_head.right
        # Delete the temporary dummy node
        vine_head = None
        return balanced_root

    # Function to perform a right rotation
    def right_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        parent.right = tmp

    # Function to perform a left rotation
    def left_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        parent.right = tmp

    # Function to perform a series of left rotations to balance the vine
    def make_rotations(self, vine_head: TreeNode, count: int):
        current = vine_head
        for _ in range(count):
            tmp = current.right
            self.left_rotate(current, tmp)
            current = current.right
