"""
Leetcode
725. Split Linked List in Parts (medium)
2023-09-06

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

    def __repr__(self) -> str:
        vals = []
        cur = self
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return str(vals)


class Solution:
    """
    Runtime: 38 ms, faster than 92.84% of Python3 online submissions for Split Linked List in Parts.
    Memory Usage: 16.6 MB, less than 97.89% of Python3 online submissions for Split Linked List in Parts.
    """

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None] * k

        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        part_len = list_len // k
        parts_with_extra_node = list_len % k

        ans = [head]

        cur = head
        cur_part_len = 1

        while cur:
            if cur_part_len >= part_len:
                if cur_part_len == part_len and parts_with_extra_node > 0:
                    parts_with_extra_node -= 1
                else:
                    next_part_root = cur.next
                    cur.next = None
                    cur = next_part_root
                    if not cur:
                        break
                    ans.append(cur)
                    cur_part_len = 1
                    continue

            cur = cur.next
            cur_part_len += 1

        if len(ans) < k:
            ans += [None] * (k - len(ans))

        return ans


class Solution1:
    """
    leetcode solution 1: create new lists
    Time: O(N + k)
    Space: O(max(N, k))
    Runtime: 47 ms, faster than 49.47% of Python3 online submissions for Split Linked List in Parts.
    Memory Usage: 16.8 MB, less than 59.37% of Python3 online submissions for Split Linked List in Parts.
    """

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        width, remainder = divmod(list_len, k)

        ans = []
        cur = head
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur:
                    cur = cur.next
            ans.append(head.next)
        return ans


class Solution2:
    """
    leetcode solution 2: split input list
    Time: O(N + k)
    Space: O(k)
    Runtime: 49 ms, faster than 40.42% of Python3 online submissions for Split Linked List in Parts.
    Memory Usage: 16.9 MB, less than 25.26% of Python3 online submissions for Split Linked List in Parts.
    """

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        width, remainder = divmod(list_len, k)

        ans = []
        cur = head
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans


def build_linked_list(arr: List[int]) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def list_to_arr(head: Optional[ListNode]) -> list:
    if not head:
        return []

    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals


s = Solution()
tests = [
    (([1, 2, 3], 5),
     [[1], [2], [3], [], []]),

    (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
     [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
]
for (raw_list, k), exp in tests:
    root = build_linked_list(raw_list)
    res = s.splitListToParts(root, k)
    res = list(map(list_to_arr, res))
    if res != exp:
        print('input:  ', raw_list)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
