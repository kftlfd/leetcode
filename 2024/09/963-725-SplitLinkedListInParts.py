"""
Leetcode
2024-09-08
725. Split Linked List in Parts
Medium

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

 

Constraints:

    The number of nodes in the list is in the range [0, 1000].
    0 <= Node.val <= 1000
    1 <= k <= 50
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 42 ms, faster than 30.76% of Python3 online submissions for Split Linked List in Parts.
    Memory Usage: 16.8 MB, less than 63.91% of Python3 online submissions for Split Linked List in Parts.
    """

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k

        if not head:
            return ans

        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        part_len, extra = divmod(list_len, k)
        part_i = 0
        cur = head
        prev = cur
        ans[0] = cur
        cur_len = 0
        while cur:
            if cur_len == part_len + (extra > 0):
                part_i += 1
                ans[part_i] = cur
                prev.next = None
                cur_len = 0
                extra -= 1
                continue
            cur_len += 1
            prev = cur
            cur = cur.next

        return ans
