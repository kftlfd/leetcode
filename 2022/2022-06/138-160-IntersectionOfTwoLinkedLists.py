"""
Leetcode
160. Intersection of Two Linked Lists (easy)
2022-06-06

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# try 1
# Time Limit Exceeded
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        remember = []
        
        curr = headA
        while curr:
            remember.append(curr)
            curr = curr.next
            
        curr = headB
        while curr:
            if curr in remember:
                return curr
            curr = curr.next
            
        return None



# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
# Runtime: 274 ms, faster than 18.30% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29.6 MB, less than 69.35% of Python3 online submissions for Intersection of Two Linked Lists.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None

        a = headA
        b = headB

        while a != b:

            if a: a = a.next
            else: a = headB

            if b: b = b.next
            else: b = headA
        
        return a



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
