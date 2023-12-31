"""
Leetcode
1721. Swapping Nodes in a Linked List (medium)
2023-05-15

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 4775 ms, faster than 5.05% of Python3 online submissions for Swapping Nodes in a Linked List.
    Memory Usage: 51 MB, less than 12.67% of Python3 online submissions for Swapping Nodes in a Linked List.
    """

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes[k-1], nodes[-k] = nodes[-k], nodes[k-1]

        new_head = nodes.pop(0)
        curr = new_head
        while nodes:
            node = nodes.pop(0)
            curr.next = node
            curr = curr.next
        curr.next = None

        return new_head
