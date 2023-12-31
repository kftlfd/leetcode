"""
Leetcode
341. Flatten Nested List Iterator (medium)
2023-10-20

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

    NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
    int next() Returns the next integer in the nested list.
    boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

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

 

Constraints:

    1 <= nestedList.length <= 500
    The values of the integers in the nested list is in the range [-10^6, 10^6].
"""

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    """
    Runtime: 61 ms, faster than 67.10% of Python3 online submissions for Flatten Nested List Iterator.
    Memory Usage: 20 MB, less than 28.24% of Python3 online submissions for Flatten Nested List Iterator.
    """

    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        for n in nestedList:
            self.arr += self._flatten(n)

    def _flatten(self, n_int: NestedInteger):
        if n_int.isInteger():
            return [n_int.getInteger()]

        arr = []
        for n in n_int.getList():
            arr += self._flatten(n)
        return arr

    def next(self) -> int:
        return self.arr.pop(0)

    def hasNext(self) -> bool:
        return len(self.arr) > 0


class NestedIterator1:
    """
    https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80247/Python-Generators-solution
    Runtime: 64 ms, faster than 50.03% of Python3 online submissions for Flatten Nested List Iterator.
    Memory Usage: 20.1 MB, less than 28.24% of Python3 online submissions for Flatten Nested List Iterator.
    """

    def __init__(self, nestedList):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)

    def next(self):
        return self.value

    def hasNext(self):
        try:
            self.value = next(self.gen)
            return True
        except StopIteration:
            return False


class NestedIterator2:
    """
    https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80146/Real-iterator-in-Python-Java-C++
    Runtime: 63 ms, faster than 55.74% of Python3 online submissions for Flatten Nested List Iterator.
    Memory Usage: 20 MB, less than 28.24% of Python3 online submissions for Flatten Nested List Iterator.
    """

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
