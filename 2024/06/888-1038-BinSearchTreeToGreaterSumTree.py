"""
Leetcode
1038. Binary Search Tree to Greater Sum Tree
Medium
2024-06-25

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:

Input: root = [0,null,1]
Output: [1,null,1]

 

Constraints:

    The number of nodes in the tree is in the range [1, 100].
    0 <= Node.val <= 100
    All the values in the tree are unique.

 

Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 40 ms, faster than 26.92% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 16.5 MB, less than 74.62% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    """

    def bstToGst(self, root: TreeNode) -> TreeNode:
        pref_sum = [0] * 101

        def dfs(node: TreeNode):
            pref_sum[node.val] = node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)

        for i in range(len(pref_sum) - 2, -1, -1):
            pref_sum[i] += pref_sum[i + 1]

        def dfs2(node: TreeNode):
            node.val = pref_sum[node.val]
            if node.left:
                dfs2(node.left)
            if node.right:
                dfs2(node.right)
        dfs2(root)

        return root


class Solution2:
    """
    leetcode solution 2: Reverse In-order Traversal
    Runtime: 42 ms, faster than 17.47% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 16.7 MB, less than 5.60% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    """

    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = [0]  # Using a list to emulate a mutable integer reference
        self.bst_to_gst_helper(root, node_sum)
        return root

    def bst_to_gst_helper(self, root, node_sum):
        # If root is null, make no changes.
        if root is None:
            return

        self.bst_to_gst_helper(root.right, node_sum)
        node_sum[0] += root.val
        # Update the value of root.
        root.val = node_sum[0]
        self.bst_to_gst_helper(root.left, node_sum)


class Solution3:
    """
    leetcode solution 3: Iterative Reverse In-order Traversal
    Runtime: 44 ms, faster than 8.02% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 16.5 MB, less than 31.32% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    """

    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        st = []
        node = root

        while st or node is not None:

            while node is not None:
                st.append(node)
                node = node.right
            # Store the top value of stack in node and pop it.
            node = st.pop()

            # Update value of node.
            node_sum += node.val
            node.val = node_sum

            # Move to the left child of node.
            node = node.left

        return root


class Solution4:
    """
    leetcode solution 4: Morris Traversal
    Runtime: 39 ms, faster than 34.73% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    Memory Usage: 16.5 MB, less than 74.62% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
    """

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root


class Solution5:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        g_sum = 0

        def dfs(node):
            nonlocal g_sum

            if not node:
                return

            dfs(node.right)
            node.val += g_sum
            g_sum = node.val
            dfs(node.left)

        dfs(root)
        return root
