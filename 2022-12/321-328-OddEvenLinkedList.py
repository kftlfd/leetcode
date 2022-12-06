"""
Leetcode
328. Odd Even Linked List (medium)
2022-12-07

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"{self.val}."
        else:
            return f"{self.val} -> {self.next}"

    def to_list(self):
        if not self.next:
            return [self.val]
        else:
            return [self.val] + self.next.to_list()


# Runtime: 101 ms
# Memory Usage: 16.5 MB
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        start_odd = head
        start_even = head.next

        odd = start_odd
        even = start_even

        last_odd = odd
        last_even = even

        while even and odd:
            odd.next = even.next
            last_odd = odd
            odd = odd.next
            if odd:
                even.next = odd.next
                last_even = even
                even = even.next

        if odd:
            last_odd = odd
        last_odd.next = start_even
        return start_odd


def make_list(vals: List) -> ListNode:
    start = ListNode()
    curr = start
    for val in vals:
        curr.next = ListNode(val)
        curr = curr.next
    return start.next


s = Solution()
tests = [
    ([1, 2, 3, 4, 5],
     [1, 3, 5, 2, 4]),

    ([2, 1, 3, 5, 6, 4, 7],
     [2, 3, 6, 7, 1, 5, 4])
]
for inp, exp in tests:
    head = make_list(inp)
    res = s.oddEvenList(head)
    out = res.to_list()
    if out != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', out)
        print()
print('Completed testing')
