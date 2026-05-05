"""
Leetcode
2026-05-05
61. Rotate List
Medium

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9


"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.32MB Beats 36.28%
    """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.get_list_len(head)
        if not head or n < 1:
            return head

        k = k % n
        if k == 0:
            return head

        last = head
        for _ in range(n - k - 1):
            last = last.next

        new_root = last.next
        last.next = None

        mid = new_root
        while mid.next:
            mid = mid.next

        mid.next = head

        return new_root

    def get_list_len(self, head: Optional[ListNode]) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l
