"""
Leetcode
234. Palindrome Linked List (easy)
2022-08-23

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f'{self.val}->{self.next}'
        else:
            return f'{self.val}.'


# Runtime: 1281 ms, faster than 42.51% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.7 MB, less than 47.91% of Python3 online submissions for Palindrome Linked List.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        node = head
        vals = []
        while node:
            vals += [node.val]
            node = node.next

        for i in range(len(vals) // 2):
            if vals[i] != vals[-(i+1)]:
                return False

        return True


# https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
# Runtime: 829 ms, faster than 92.11% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 38.8 MB, less than 89.07% of Python3 online submissions for Palindrome Linked List.
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:  # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


s = Solution()
tests = [
    [1, 2, 2, 1],
    [1, 2],
]
for t in tests:
    headptr = ListNode()
    curr = headptr
    for v in t:
        curr.next = ListNode(val=v)
        curr = curr.next
    head = headptr.next
    print(head)
    print(s.isPalindrome(head))
    print()
