'''
Leetcode
1305. All Elements in Two Binary Search Trees (medium)
2022-01-26
'''

import unittest

# Given two binary search trees root1 and root2, 
# return a list containing all the integers from both trees 
# sorted in ascending order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

class Solution:

    # create lists from binary tree roots, merge them, sort the result
    def getAllElements(self, root1, root2):
        
        # generate list from binary tree root (exclude None values)
        def treeList(root):
            # base cases
            if root == None:
                return []
            if root.left == None and root.right == None:
                if root.val == None:
                    return []
                return [root.val]
            # recursive case
            out = [root.val]
            out += treeList(root.left)
            out += treeList(root.right)
            return out
        
        out = treeList(root1) + treeList(root2)
        return sorted(out)

    
    # basically the same as previous but more optimized
    # credits to @artod:
    # https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/1720024/Python3-6-LINES-(_-)-Explained
    def getAllElements2(self, root1, root2):

        # generate list (sorted, asc) from binary tree root
        def treeList(root):
            # base cases
            if root == None: return []
            # recursive case
            return treeList(root.left) + [root.val] + treeList(root.right)
        
        t1, t2, out = treeList(root1), treeList(root2), []

        # merge lists to [out]:
        # compare first elements, pop smallest to [out], do until one (or both) list runs out
        # add to [out] elements from the list that's left (if any)
        while t1 and t2:
            out.append( t1.pop(0) if t1[0] < t2[0] else t2.pop(0) )
        return out + (t1 or t2)



# too lazy to create actual binary trees, so no testting this time
'''
sol = Solution()
tests = [
    # {'root1': [], 'root2': [], 'out': []},
    {'root1': [1], 'root2': [2], 'out': [1,2]},
    {'root1': [2,1,4], 'root2': [1,0,3], 'out': [0,1,1,2,3,4]},
    {'root1': [1,None,8], 'root2': [8,1], 'out': [1,1,8,8]},
]
class SolutionTest(unittest.TestCase):
    def test_solution(self):
        for test in tests:
            self.assertEqual(sol.getAllElements(test['root1'], test['root2']), test['out'])

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    for test in tests:
        print('test:', test, '\nout :', sol.getAllElements(test['root1'], test['root2']) )
'''