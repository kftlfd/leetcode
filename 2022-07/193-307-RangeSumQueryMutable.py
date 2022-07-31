"""
Leetcode
307. Range Sum Query - Mutable (medium)
2022-07-31

Given an integer array nums, handle multiple queries of the following types:

 1. Update the value of an element in nums.
 2. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

 - NumArray(int[] nums) Initializes the object with the integer array nums.
 - void update(int index, int val) Updates the value of nums[index] to be val.
 - int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
"""

from typing import List

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# python lazy - Time Limit Exceeded
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# https://leetcode.com/problems/range-sum-query-mutable/discuss/2359788/esiest-python-solution-easy-to-understand
# Runtime: 1590 ms, faster than 94.25% of Python3 online submissions for Range Sum Query - Mutable.
# Memory Usage: 30.9 MB, less than 85.17% of Python3 online submissions for Range Sum Query - Mutable.
class NumArray1:

    def __init__(self, nums: List[int]):
        self.num_array = nums
        self.pre_sum = sum(self.num_array)

    def update(self, index: int, val: int) -> None:
        self.pre_sum = self.pre_sum - self.num_array[index] + val
        self.num_array[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum - sum(self.num_array[:left]) - sum(self.num_array[right+1:])


tests = [
    (["NumArray", "sumRange", "update", "sumRange"],
     [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]])
]
for commands, inputs in tests:
    s = None
    out = []
    for i in range(len(commands)):
        if commands[i] == "NumArray":
            s = NumArray1(*inputs[i])
            out.append(None)
        elif commands[i] == "sumRange":
            out.append(s.sumRange(*inputs[i]))
        elif commands[i] == "update":
            s.update(*inputs[i])
            out.append(None)
    print("Input:")
    print(commands)
    print(inputs)
    print("Output:")
    print(out, '\n')
