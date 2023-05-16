"""
Leetcode
24. Swap Nodes in Pairs (medium)
2023-05-16

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 48 ms, faster than 16.98% of Python3 online submissions for Swap Nodes in Pairs.
    Memory Usage: 16.3 MB, less than 23.07% of Python3 online submissions for Swap Nodes in Pairs.
    """

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second
