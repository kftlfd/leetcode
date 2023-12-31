"""
Leetcode
284. Peeking Iterator (medium)
2022-04-25

Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

 - PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
 - int next() Returns the next element in the array and moves the pointer to the next element.
 - boolean hasNext() Returns true if there are still elements in the array.
 - int peek() Returns the next element in the array without moving the pointer.

Note: Each language may have a different implementation of the constructor and Iterator, but they all support the int next() and boolean hasNext() functions.
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].



# try 1
# Runtime: 40 ms, faster than 66.01% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.1 MB, less than 29.71% of Python3 online submissions for Peeking Iterator.
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.data = []
        while iterator.hasNext():
            self.data.append(iterator.next())
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.data[0]        

    def next(self):
        """
        :rtype: int
        """
        return self.data.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.data) > 0



# Runtime: 34 ms, faster than 84.51% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.1 MB, less than 29.71% of Python3 online submissions for Peeking Iterator.
class PeekingIterator1:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.nxt = None
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()
            
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nxt

    def next(self):
        """
        :rtype: int
        """
        out = self.nxt        
        self.nxt = self.iterator.hasNext()
        if self.nxt:
            self.nxt = self.iterator.next()        
        return out

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt != False



# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()
