"""
Leetcode
341. Flatten Nested List Iterator (medium)
2022-05-08

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

 - NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
 - int next() Returns the next integer in the nested list.
 - boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:

    initialize iterator with nestedList
    res = []
    while iterator.hasNext()
        append iterator.next() to the end of res
    return res

If res matches the expected flattened list, then your code will be judged as correct.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



# try 1
# Runtime: 77 ms, faster than 65.41% of Python3 online submissions for Flatten Nested List Iterator.
# Memory Usage: 17.8 MB, less than 41.16% of Python3 online submissions for Flatten Nested List Iterator.
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
            
        self.flist = []
        def unnest(n):
            if n.isInteger():
                self.flist.append(n.getInteger())
            else:
                for x in n.getList(): unnest(x)
        for n in nestedList:
            unnest(n)
        
        self.curr = 0
        self.length = len(self.flist)
        
    
    def next(self) -> int:
        out = self.flist[self.curr]
        self.curr += 1
        return out
        
    
    def hasNext(self) -> bool:
        return self.curr < self.length
         


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
