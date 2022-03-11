'''
Leetcode
61. Rotate List (medium)
2022-03-11

Given the head of a linked list, rotate the list to the right by k places.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if not self.next: return f"({self.val})."
        return f"({self.val})-> {self.next}"



# try 1
# Runtime: 32 ms, faster than 97.66% of Python3 online submissions for Rotate List.
# Memory Usage: 13.9 MB, less than 88.66% of Python3 online submissions for Rotate List.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0: return head
        
        # find the lenght of linked list
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
            
        # reduce k to length of linked list
        k = k % l
        if k == 0: return head
        
        ### rotate
        
        # split
        new_head = head
        for i in range(l - k - 1):
            new_head = new_head.next
        tail = new_head
        new_head = new_head.next
        tail.next = None
            
        # join
        new_tail = new_head
        while new_tail.next:
            new_tail = new_tail.next
        new_tail.next = head
        
        return new_head
        


s = Solution()
tests = [
    [[1], 0],
    [[1,2], 1],
    [[1,2,3,4,5], 2],
    [[0,1,2], 4]
]
for t in tests:

    list = ListNode()
    curr = list
    for val in t[0]:
        curr.next = ListNode(val)
        curr = curr.next
    list = list.next

    print("test: ", list, "rotate: ", t[1])
    print("out:  ", s.rotateRight(list, t[1]))
    print()
