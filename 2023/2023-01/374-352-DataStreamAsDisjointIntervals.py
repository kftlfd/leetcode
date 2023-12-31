"""
Leetcode
352. Data Stream as Disjoint Intervals (hard)
2023-01-28

Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

    SummaryRanges() Initializes the object with an empty stream.
    void addNum(int value) Adds the integer value to the stream.
    int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.

Example 1:
Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
"""

from typing import List, Optional


# Runtime: 499 ms, faster than 25.00% of Python3 online submissions for Data Stream as Disjoint Intervals.
# Memory Usage: 18.9 MB, less than 76.30% of Python3 online submissions for Data Stream as Disjoint Intervals.
class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for num in sorted(self.nums):
            if not intervals or intervals[-1][1] != num - 1:
                intervals.append([num, num])
            else:
                intervals[-1][1] = num
        return intervals


tests = [
    (
        (
            ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
             "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
            [[], [1], [], [3], [], [7], [], [2], [], [6], []]
        ),
        [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None, [
            [1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]]
    ),
]
for inp, exp in tests:
    res = []
    s = None
    for command, inpt in zip(*inp):
        if command == "SummaryRanges":
            s = SummaryRanges()
            res.append(None)
        elif command == "addNum":
            res.append(s.addNum(*inpt))
        elif command == "getIntervals":
            res.append(s.getIntervals())
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
