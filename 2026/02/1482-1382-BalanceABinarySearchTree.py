"""
Leetcode
2026-02-09
1382. Balance a Binary Search Tree
Medium

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
    1 <= Node.val <= 10^5


Hint 1
Convert the tree to a sorted array using an in-order traversal.
Hint 2
Construct a new balanced tree from the sorted array recursively.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution01:
    """
    Runtime 38ms Beats 34.03%
    Memory 23.84MB Beats 55.13%
    """

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = self.to_list(root)
        return self.to_tree(vals)

    def to_list(self, root: Optional[TreeNode]) -> List[int]:
        vals_list = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            vals_list.append(node.val)
            traverse(node.right)

        traverse(root)
        return vals_list

    def to_tree(self, vals_list: List[int]) -> Optional[TreeNode]:
        if not vals_list:
            return None

        mid = len(vals_list) // 2
        node = TreeNode(vals_list[mid])
        node.left = self.to_tree(vals_list[:mid])
        node.right = self.to_tree(vals_list[mid+1:])
        return node


class Solution02:
    """
    in-place
    Runtime 23ms Beats 90.19%
    Memory 24.41MB Beats 40.56%
    """

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = self.to_list(root)
        return self.to_tree(nodes)

    def to_list(self, root: Optional[TreeNode]) -> List[TreeNode]:
        nodes_list = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            nodes_list.append(node)
            traverse(node.right)

        traverse(root)
        return nodes_list

    def to_tree(self, vals_list: List[TreeNode]) -> Optional[TreeNode]:
        if not vals_list:
            return None

        mid = len(vals_list) // 2
        node = vals_list[mid]
        node.left = self.to_tree(vals_list[:mid])
        node.right = self.to_tree(vals_list[mid+1:])
        return node


class Solution2:
    """
    leetcode solution 2: Day-Stout-Warren Algorithm / In-Place Balancing
    Runtime 24ms Beats 87.07%
    Memory 23.32MB Beats 64.49%
    """

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
