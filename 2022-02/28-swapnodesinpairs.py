'''
Leetcode
24. Swap Nodes in Pairs (medium)
2022-02-16

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's 
nodes (i.e., only nodes themselves may be changed.)
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        n = self.next.val if self.next else "N"
        return f"({self.val}-{n})"



# Try 1
# Runtime: 47 ms, faster than 39.56% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14 MB, less than 75.41% of Python3 online submissions for Swap Nodes in Pairs.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        one = head
        if not one or not one.next: return one
        two = one.next
        prev = None
        out = two
        
        while two:
            tmp1 = one
            tmp2 = two
            tmp3 = two.next

            if prev:
                prev.next = tmp2
            two.next = one
            one.next = tmp3

            prev = one
            one = one.next
            if not one or not one.next: break
            two = one.next
            
        return out
        


# Try 2
# recursion
# Runtime: 52 ms, faster than 28.36% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14 MB, less than 75.41% of Python3 online submissions for Swap Nodes in Pairs.
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case
        if not head or not head.next:
            return head
        
        # recursive case
        tmp3 = head.next.next
        tmp2 = head.next
        tmp1 = head
        
        tmp2.next = tmp1
        tmp1.next = self.swapPairs(tmp3)
        
        return tmp2



solution = Solution2()
tests = [
    [],
    [1],
    [1,2,3,4,5,6,7]
]

for test in tests:

    # create linked list
    vals = test
    root = ListNode()
    next = root
    for i in range(len(vals)):
        next.val = vals[i]
        if i != len(vals) - 1:
            next.next = ListNode()
            next = next.next

    # print list
    l = []
    ln = root
    while ln:
        l.append(ln.val)
        ln = ln.next
    print("test: ", l)

    # print swaped
    swaped_root = solution.swapPairs(root)
    out = []
    while swaped_root:
        out.append(swaped_root.val)
        swaped_root = swaped_root.next
    print("out:  ", out, "\n")