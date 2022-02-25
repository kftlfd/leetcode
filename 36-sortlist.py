'''
Leetcode
148. Sort List (medium)
2022-02-24

Given the head of a linked list, return the list after sorting it in ascending order.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if self.next:
            return f'{self.val}-> {self.next}'
        return f'{self.val}.'



# Runtime error
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return head
        
        from queue import PriorityQueue

        pq = PriorityQueue()

        node = head
        while node:
            pq.put((node.val, node))
            node = node.next

        out = pq.get()[1]
        curr = out
        while pq.queue:
            curr.next = pq.get()[1]
            curr = curr.next
        curr.next = None

        return out



# Runtime: 434 ms, faster than 67.79% of Python3 online submissions for Sort List.
# Memory Usage: 32.8 MB, less than 23.62% of Python3 online submissions for Sort List.
class Solution2:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return head
        
        nodes = []

        node = head
        while node:
            tmp = node.next
            node.next = None
            nodes.append((node.val, node))
            node = tmp

        nodes.sort(key=lambda x: x[0])

        out = nodes.pop(0)[1]
        curr = out
        while nodes:
            curr.next = nodes.pop(0)[1]
            curr = curr.next
        curr.next = None

        return out



class Solution3:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return head
        
        nodes = []

        node = head
        while node:
            tmp = node.next
            node.next = None
            nodes.append(node)
            node = tmp

        nodes.sort(key=lambda x: x.val)

        out = nodes.pop(0)
        curr = out
        while nodes:
            curr.next = nodes.pop(0)
            curr = curr.next

        return out



vals = [4,19,14,5,-3,1,8,5,11,15]
head = ListNode()
tmp = head
while vals:
    tmp.val = vals.pop(0)
    if vals:
        tmp.next = ListNode()
        tmp = tmp.next

Solution3().sortList(head)