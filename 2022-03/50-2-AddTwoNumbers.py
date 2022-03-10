'''
Leetcode
2. Add Two Numbers (medium)
2022-03-10

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their 
nodes contains a single digit. Add the two numbers and return the sum 
as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        if not self.next: return f"({self.val})."
        else: return f"({self.val})-> {self.next}"



# try 1
# Runtime: 106 ms, faster than 40.14% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 93.12% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = 0
        
        # add first list
        n = 0
        while l1:
            res += l1.val * (10 ** n)
            l1 = l1.next
            n += 1
            
        # add second list
        n = 0
        while l2:
            res += l2.val * (10 ** n)
            l2 = l2.next
            n += 1
            
        # convert sum to linked list
        digits = [int(n) for n in str(res)][::-1]
        head = ListNode(val=digits[0])
        curr = head
        for i in range(1, len(digits)):
            curr.next = ListNode(val=digits[i])
            curr = curr.next
            
        return head



# try 2
# Runtime: 115 ms, faster than 29.73% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 93.12% of Python3 online submissions for Add Two Numbers.
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res = ListNode()
        curr = res
        carry = 0
        
        while l1 or l2 or carry:
            
            # calc values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + carry
            
            # add node
            curr.next = ListNode()
            curr = curr.next
            curr.val = s % 10
            
            # prepare for next digit
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            carry = s // 10
        
        return res.next



s = Solution1()
tests = [
    [[2,4,3], [5,6,4]],
    [[0], [0]],
    [[9,9,9,9,9,9,9], [9,9,9,9]]
]
for t in tests:

    # create linked lists
    if t[0]:
        l1 = ListNode()
        curr = l1
        for i in range(len(t[0])):
            curr.next = ListNode(t[0][i])
            curr = curr.next
        l1 = l1.next
    else:
        l1 = None
    
    if t[1]:
        l2 = ListNode()
        curr = l2
        for i in range(len(t[1])):
            curr.next = ListNode(t[1][i])
            curr = curr.next
        l2 = l2.next
    else:
        l2 = None

    print(t)
    print(s.addTwoNumbers(l1, l2), '\n')
