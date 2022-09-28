"""
Leetcode
19. Remove Nth Node From End of List (medium)
2022-09-28

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/8802/3-short-Python-solutions
# Runtime: 56 ms, faster than 51.20% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.9 MB, less than 70.33% of Python3 online submissions for Remove Nth Node From End of List.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
