"""
Leetcode
86. Partition List (medium)
2022-07-22

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""

from typing import Optional


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


# leetcode solution
# https://leetcode.com/problems/partition-list/solution/
# Runtime: 59 ms, faster than 37.99% of Python3 online submissions for Partition List.
# Memory Usage: 14 MB, less than 31.57% of Python3 online submissions for Partition List.
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        # before and after are the two pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next


def make_list(vals: List[int]) -> ListNode:
    root = ListNode()
    curr = root
    for v in vals:
        curr.next = ListNode(val=v)
        curr = curr.next
    return root.next


s = Solution()
tests = [
    ([1, 4, 3, 2, 5, 2], 3),
    ([2, 1], 2),
]

for t in tests:
    l = make_list(t[0])
    print(l)
    print(s.partition(l, t[1]))
    print()
