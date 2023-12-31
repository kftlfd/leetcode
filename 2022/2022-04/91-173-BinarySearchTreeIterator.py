"""
Leetcode
173. Binary Search Tree Iterator (medium)
2022-04-20

Implement the BSTIterator class that represents an iterator over the 
in-order traversal of a binary search tree (BST):

 - BSTIterator(TreeNode root) Initializes an object of the BSTIterator 
   class. The root of the BST is given as part of the constructor. The 
   pointer should be initialized to a non-existent number smaller than 
   any element in the BST.
 - boolean hasNext() Returns true if there exists a number in the 
   traversal to the right of the pointer, otherwise returns false.
 - int next() Moves the pointer to the right, then returns the number 
   at the pointer.

Notice that by initializing the pointer to a non-existent smallest 
number, the first call to next() will return the smallest element in 
the BST.

You may assume that next() calls will always be valid. That is, there 
will be at least a next number in the in-order traversal when next() is 
called.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



# try 1
# Runtime: 130 ms, faster than 19.23% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 19.9 MB, less than 98.69% of Python3 online submissions for Binary Search Tree Iterator.
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.q = [root]
        while self.q:
            node = self.q.pop(0)
            if node.left: self.q.append(node.left)
            if node.right: self.q.append(node.right)
            self.st.append(node.val)
        self.st.sort()

    def next(self) -> int:
        return self.st.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.st)



# https://leetcode.com/problems/binary-search-tree-iterator/discuss/52642/Two-Python-solutions-stack-and-generator
# Runtime: 84 ms, faster than 69.75% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 20.4 MB, less than 35.61% of Python3 online submissions for Binary Search Tree Iterator.
class BSTIterator1:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0



s = Solution()
tests = [
]
print("no tests")
# for t in tests:
#     print(t)
#     print()
