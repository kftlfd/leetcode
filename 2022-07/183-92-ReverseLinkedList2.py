"""
Leetcode
92. Reverse Linked List II (medium)
2022-07-21

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"{self.val}."
        else:
            return f"{self.val}->{self.next}"


# Runtime: 52 ms, faster than 41.07% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 13.8 MB, less than 98.94% of Python3 online submissions for Reverse Linked List II.
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        i = 1
        curr = head

        # find left end
        if i == left:
            reverse_left = head
            left_end = None
        else:
            while curr:
                i += 1
                if i == left:
                    reverse_left = curr.next
                    left_end = curr
                    break
                curr = curr.next
            curr = curr.next

        # find right end
        while curr:
            if i == right:
                reverse_right = curr
                right_end = curr.next
                break
            i += 1
            curr = curr.next

        # reverse
        reverse_right.next = None
        reversed_left, reversed_right = self.reverseList(reverse_left)

        # reconnect list
        if left_end:
            left_end.next = reversed_left
        reversed_right.next = right_end

        return head if left_end else reversed_left

    def reverseList(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        reversed_end = head
        reversed_start = head
        curr_original = head.next
        curr_reversed = head.next

        reversed_end.next = None

        while curr_original:
            curr_original = curr_original.next
            curr_reversed.next = reversed_start
            reversed_start = curr_reversed
            curr_reversed = curr_original

        return (reversed_start, reversed_end)


# https://leetcode.com/problems/reverse-linked-list-ii/discuss/1291559/Python-O(1)O(n)-spacetime-solution-explained
# Runtime: 57 ms, faster than 27.28% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14 MB, less than 87.01% of Python3 online submissions for Reverse Linked List II.
class Solution1:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next

        curr = pre.next
        nxt = curr.next

        for i in range(n-m):
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp

        pre.next.next = nxt
        pre.next = curr
        return dummy.next


s = Solution()
tests = [
    ([1, 2, 3, 4, 5], 2, 4),
    ([5], 1, 1),
    ([3, 5], 1, 2),
]


def make_list(vals: List[int]) -> ListNode:
    root = ListNode()
    curr = root
    for v in vals:
        curr.next = ListNode(val=v)
        curr = curr.next
    return root.next


for t in tests:
    l = make_list(t[0])
    print(l, t[1], t[2])
    print(s.reverseBetween(l, t[1], t[2]))
    print()
