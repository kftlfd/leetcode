"""
Leetcode
2025-02-23
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]

 

Constraints:

    1 <= preorder.length <= 30
    1 <= preorder[i] <= preorder.length
    All the values of preorder are unique.
    postorder.length == preorder.length
    1 <= postorder[i] <= postorder.length
    All the values of postorder are unique.
    It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.


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
    Runtime 0ms Beats 100.00%
    Memory 17.86MB Beats 50.51%
    """

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        node = TreeNode(preorder[0])

        if len(preorder) > 1:
            left_val = preorder[1]
            right_val = postorder[-2]

            if left_val != right_val:
                left_pre_idx = 1
                left_post_idx = postorder.index(left_val)

                right_pre_idx = preorder.index(right_val)
                right_post_idx = -2

                left_preorder = preorder[left_pre_idx:right_pre_idx]
                left_postorder = postorder[:left_post_idx+1]
                node.left = self.constructFromPrePost(
                    left_preorder, left_postorder)

                right_preorder = preorder[right_pre_idx:]
                right_postorder = postorder[left_post_idx+1:right_post_idx+1]
                node.right = self.constructFromPrePost(
                    right_preorder, right_postorder)
            else:
                node.left = self.constructFromPrePost(
                    preorder[1:], postorder[:-1])

        return node


class Solution1:
    """
    leetcode solution 1: Divide and Conquer
    Runtime 3ms Beats 50.00%
    Memory 17.74MB Beats 71.53%
    """

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        num_of_nodes = len(preorder)
        return self._construct_tree(0, num_of_nodes - 1, 0, preorder, postorder)

    # Helper function to construct the tree recursively
    def _construct_tree(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        postorder: List[int],
    ) -> Optional[TreeNode]:
        # Base case: If there are no nodes to process, return None
        if pre_start > pre_end:
            return None

        # Base case: If only one node is left, return that node
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        # The left child root in preorder traversal (next element after root)
        left_root = preorder[pre_start + 1]

        # Calculate the number of nodes in the left subtree by searching in postorder
        num_of_nodes_in_left = 1
        while postorder[post_start + num_of_nodes_in_left - 1] != left_root:
            num_of_nodes_in_left += 1

        root = TreeNode(preorder[pre_start])

        # Recursively construct the left subtree
        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            postorder,
        )

        # Recursively construct the right subtree
        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            postorder,
        )

        return root


class Solution2:
    """
    leetcode solution 2: Using Index Array
    Runtime 0ms Beats 100.00%
    Memory 17.70MB Beats 71.53%
    """

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        num_of_nodes = len(preorder)

        # Create the index list for `postorder`
        index_in_post_order = [0] * (num_of_nodes + 1)
        for index in range(num_of_nodes):
            # Store the index of the current element
            index_in_post_order[postorder[index]] = index

        return self._construct_tree(
            0, num_of_nodes - 1, 0, preorder, index_in_post_order
        )

    # Helper function to construct the tree recursively
    def _construct_tree(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        index_in_post_order: List[int],
    ) -> Optional[TreeNode]:
        # Base case: If there are no nodes to process, return None
        if pre_start > pre_end:
            return None

        # Base case: If only one node is left, return that node
        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        # The left child root in preorder traversal (next element after root)
        left_root = preorder[pre_start + 1]

        # Calculate the number of nodes in the left subtree by searching in postorder
        num_of_nodes_in_left = index_in_post_order[left_root] - post_start + 1

        root = TreeNode(preorder[pre_start])

        # Recursively construct the left subtree
        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            index_in_post_order,
        )

        # Recursively construct the right subtree
        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            index_in_post_order,
        )

        return root


class Solution3:
    """
    leetcode solution 3: Optimized Recursion
    Runtime 0ms Beats 100.00%
    Memory 17.86MB Beats 50.51%
    """

    pre_index = 0
    post_index = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        self.post_index = 0
        return self._construct_tree(preorder, postorder)

    def _construct_tree(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1

        # Recursively construct the left subtree if the root is not the last of
        # its subtree
        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)

        # Recursively construct the right subtree if the root is not the last of
        # its subtree
        if root.val != postorder[self.post_index]:
            root.right = self._construct_tree(preorder, postorder)

        # Mark this node and its subtree as fully processed
        self.post_index += 1
        return root
