"""
Leetcode
109. Convert Sorted List to Binary Search Tree (medium)
2023-03-11

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Runtime: 116 ms, faster than 94.04% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
    Memory Usage: 20.3 MB, less than 26.39% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
    """

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        def get_tree_node(vals: List[int]) -> TreeNode:
            if not vals:
                return None
            mid = len(vals) // 2
            return TreeNode(
                val=vals[mid],
                left=get_tree_node(vals[:mid]),
                right=get_tree_node(vals[mid+1:])
            )

        return get_tree_node(vals)
