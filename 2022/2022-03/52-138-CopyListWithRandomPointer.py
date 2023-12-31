'''
Leetcode
138. Copy List with Random Pointer (medium)
2022-03-12

A linked list of length n is given such that each node contains an 
additional random pointer, which could point to any node in the list, 
or null.

Construct a deep copy of the list. The deep copy should consist of 
exactly n brand new nodes, where each new node has its value set to 
the value of its corresponding original node. Both the next and random 
pointer of the new nodes should point to new nodes in the copied list 
such that the pointers in the original list and copied list represent 
the same list state. None of the pointers in the new list should point 
to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where 
X.random --> Y, then for the corresponding two nodes x and y in the 
copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

 - val: an integer representing Node.val
 - random_index: the index of the node (range from 0 to n-1) that the 
   random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

https://leetcode.com/problems/copy-list-with-random-pointer/
'''

from typing import Optional
from collections import OrderedDict

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



# try 1
# Runtime: 64 ms, faster than 24.56% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.9 MB, less than 85.83% of Python3 online submissions for Copy List with Random Pointer.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return head

        # dummy starter for copy of linked list
        copy = Node(0)

        # remember og and copied nodes
        og = []
        cp = []

        # go through og list, copy it and remember both lists (without pointers to random)
        curr_og = head
        curr_cp = copy
        while curr_og:
            curr_cp.next = Node(curr_og.val)
            og.append(curr_og)
            cp.append(curr_cp.next)
            curr_og = curr_og.next
            curr_cp = curr_cp.next

        # write pointers to random to copied list
        curr_og = head
        curr_cp = copy.next
        while curr_og:
            if curr_og.random:
                curr_cp.random = cp[ og.index(curr_og.random) ]
            curr_og = curr_og.next
            curr_cp = curr_cp.next
        
        return copy.next



# https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1841010/Python3-JUST-TWO-STEPS-()-Explained
# Runtime: 39 ms, faster than 82.62% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15 MB, less than 29.48% of Python3 online submissions for Copy List with Random Pointer.
class Solution1:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return head
        
        copy = Node(0)
        hashmap = {}
        
        og = head
        cp = copy
        while og:
            cp.next = Node(og.val)
            hashmap[og] = cp.next
            cp = cp.next
            og = og.next
            
        og = head
        cp = copy.next
        while og:
            if og.random:
                cp.random = hashmap[og.random]
            cp = cp.next
            og = og.next
            
        return copy.next



# no tests this time