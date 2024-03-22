"""
Leetcode
234. Palindrome Linked List
Easy
2024-03-22

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 482 ms, faster than 5.03% of Python3 online submissions for Palindrome Linked List.
    Memory Usage: 37.7 MB, less than 8.68% of Python3 online submissions for Palindrome Linked List.
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = self.create_reversed(head)
        cur1 = head
        cur2 = rev

        while cur1:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        return True

    def create_reversed(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        while cur:
            node = ListNode(cur.val, dummy.next)
            dummy.next = node
            cur = cur.next
        return dummy.next
