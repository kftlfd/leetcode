"""
Leetcode
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Medium
2024-07-05

A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

 

Example 1:

Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:

Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:

Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

 

Constraints:

    The number of nodes in the list is in the range [2, 10^5].
    1 <= Node.val <= 10^5
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if not self.next:
            return f"{self.val}"
        return f"{self.val} -> {self.next}"


class Solution:
    """
    Runtime: 376 ms, faster than 22.43% of Python3 online submissions for Find the Minimum and Maximum Number of Nodes Between Critical Points.
    Memory Usage: 44.4 MB, less than 58.17% of Python3 online submissions for Find the Minimum and Maximum Number of Nodes Between Critical Points.
    """

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]

        min_d = float('inf')
        max_d = 0

        prev_val = head.val
        cur = head.next
        cur_i = 1
        first_crit_i = None
        last_crit_i = None

        while cur and cur.next:
            if (cur.val > prev_val and cur.val > cur.next.val) or (cur.val < prev_val and cur.val < cur.next.val):
                if last_crit_i is not None:
                    min_d = min(min_d, cur_i - last_crit_i)
                    max_d = max(max_d, cur_i - first_crit_i)
                else:
                    first_crit_i = cur_i
                last_crit_i = cur_i

            prev_val = cur.val
            cur = cur.next
            cur_i += 1

        return [min_d, max_d] if max_d != 0 else [-1, -1]


def createList(vals: List[int]) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


s = Solution()
tests = [
    ([5, 3, 1, 2, 5, 1, 2],
     [1, 3]),
]
for inp, exp in tests:
    res = s.nodesBetweenCriticalPoints(createList(inp))
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
