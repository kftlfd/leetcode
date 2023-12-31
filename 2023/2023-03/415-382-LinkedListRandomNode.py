"""
Leetcode
382. Linked List Random Node (medium)
2023-03-10

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

    Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
    int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
"""

from typing import Optional
import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


class Solution:
    """
    Runtime: 70 ms, faster than 83.83% of Python3 online submissions for Linked List Random Node.
    Memory Usage: 17.2 MB, less than 97.21% of Python3 online submissions for Linked List Random Node.
    """

    def __init__(self, head: Optional[ListNode]):
        self.range = []
        while head:
            self.range.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.range)


class Solution1:
    """
    leetcode solution 2: Reservoir Sampling
    Runtime: 88 ms, faster than 38.29% of Python3 online submissions for Linked List Random Node.
    Memory Usage: 17.4 MB, less than 49.63% of Python3 online submissions for Linked List Random Node.
    """

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        chosen_value = 0
        curr = self.head
        while curr:
            if random.random() < 1 / scope:
                chosen_value = curr.val
            curr = curr.next
            scope += 1
        return chosen_value
