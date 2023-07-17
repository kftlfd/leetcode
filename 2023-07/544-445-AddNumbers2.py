"""
Leetcode
445. Add Two Numbers II (medium)
2023-07-17

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 73 ms, faster than 92.55% of Python3 online submissions for Add Two Numbers II.
    Memory Usage: 16.5 MB, less than 31.76% of Python3 online submissions for Add Two Numbers II.
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        cur1 = l1
        cur2 = l2
        while cur1:
            num1 *= 10
            num1 += cur1.val
            cur1 = cur1.next
        while cur2:
            num2 *= 10
            num2 += cur2.val
            cur2 = cur2.next

        ans = ListNode()
        cur = ans

        for digit in str(num1 + num2):
            cur.next = ListNode(int(digit))
            cur = cur.next

        return ans.next


class Solution1:
    """
    leetcode solution 2: Reverse Given Linked Lists
    Runtime: 72 ms, faster than 94.36% of Python3 online submissions for Add Two Numbers II.
    Memory Usage: 16.3 MB, less than 68.70% of Python3 online submissions for Add Two Numbers II.
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)

        total_sum = 0
        carry = 0
        ans = ListNode()
        while r1 or r2:
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next

            ans.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry

        return ans.next if carry == 0 else ans

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
