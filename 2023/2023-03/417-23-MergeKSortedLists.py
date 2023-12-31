"""
Leetcode
23. Merge k Sorted Lists (hard)
2023-03-12

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.to_array()}"

    def to_array(self):
        if self.next:
            return [self.val] + self.next.to_array()
        return [self.val]

    @staticmethod
    def from_array(arr: List[int]):
        if not arr:
            return None
        dummy = ListNode()
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next


class Solution:
    """
    brute force
    Runtime: 4829 ms, faster than 8.06% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 17.5 MB, less than 89.24% of Python3 online submissions for Merge k Sorted Lists.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        lists = [l for l in lists if l]

        head = ListNode()

        curr = head

        while lists:
            curr_min = 0

            for i in range(1, len(lists)):
                if lists[i].val < lists[curr_min].val:
                    curr_min = i

            curr.next = lists.pop(curr_min)

            curr = curr.next

            if curr.next:
                lists.append(curr.next)

        return head.next


class Solution1:
    """
    priority queue
    Runtime: 95 ms, faster than 91.20% of Python3 online submissions for Merge k Sorted Lists.
    Memory Usage: 18.2 MB, less than 35.86% of Python3 online submissions for Merge k Sorted Lists.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        q = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(q, (node.val, i, node))

        head = ListNode()
        curr = head

        while q:

            _, i, node = heapq.heappop(q)

            curr.next = node

            curr = curr.next

            if curr.next:
                heapq.heappush(q, (curr.next.val, i, curr.next))

        return head.next


s = Solution1()
tests = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]],
     [1, 1, 2, 3, 4, 4, 5, 6]),

    ([],
     []),

    ([[]],
     []),
]
for inp, exp in tests:
    lists_arr = [ListNode.from_array(arr) for arr in inp]
    res = s.mergeKLists(lists_arr)
    res = res.to_array() if res else []
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
