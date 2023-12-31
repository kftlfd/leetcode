"""
Leetcode
237. Delete Node in a Linked List (medium)
2022-10-13

There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

 - The value of the given node should not exist in the linked list.
 - The number of nodes in the linked list should decrease by one.
 - All the values before node should be in the same order.
 - All the values after node should be in the same order.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# trick problem, expects not actually deleting the given node,
# but rather overwritting it with the next one
# Runtime: 45 ms, faster than 87.87% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.3 MB, less than 53.03% of Python3 online submissions for Delete Node in a Linked List.
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
