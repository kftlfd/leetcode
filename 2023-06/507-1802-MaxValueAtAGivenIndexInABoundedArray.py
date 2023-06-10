"""
Leetcode
1802. Maximum Value at a Given Index in a Bounded Array (medium)
2023-06-10

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

    nums.length == n
    nums[i] is a positive integer where 0 <= i < n.
    abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    The sum of all the elements of nums does not exceed maxSum.
    nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].

Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3

Constraints:

    1 <= n <= maxSum <= 10^9
    0 <= index < n
"""


class Solution:
    """
    wrong answer
    """

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left_count = index
        right_count = n - index - 1

        def is_valid(value: int) -> bool:
            # arr = [0] * n
            # arr[index] = value
            # arr[:index] = [max(0, value - v - 1) for v in range(left_count)][::-1]
            # arr[index+1:] = [max(0, value - v - 1) for v in range(right_count)]
            left_sum = sum(range(max(0, value - left_count), value))
            right_sum = sum(range(max(0, value - right_count), value))
            return left_sum + value + right_sum <= maxSum

        left = 0
        right = maxSum

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


class Solution1:
    """
    leetcode solution
    Runtime: 50 ms, faster than 54.62% of Python3 online submissions for Maximum Value at a Given Index in a Bounded Array.
    Memory Usage: 16.1 MB, less than 68.46% of Python3 online submissions for Maximum Value at a Given Index in a Bounded Array.
    """

    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0

        # On index's left:
        # If value > index, there are index + 1 numbers in the arithmetic sequence:
        # [value - index, ..., value - 1, value].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [1, 2, ..., value - 1, value], plus a sequence of length (index - value + 1) of 1s.
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1

        # On index's right:
        # If value >= n - index, there are n - index numbers in the arithmetic sequence:
        # [value, value - 1, ..., value - n + 1 + index].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [value, value - 1, ..., 1], plus a sequence of length (n - index - value) of 1s.
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value

        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left


class Solution2:
    """
    https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1119801/JavaC++Python-Binary-Search
    Runtime: 55 ms, faster than 38.46% of Python3 online submissions for Maximum Value at a Given Index in a Bounded Array.
    Memory Usage: 16.4 MB, less than 30.00% of Python3 online submissions for Maximum Value at a Given Index in a Bounded Array.
    """

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1


s = Solution1()
tests = [
    ((4, 0, 4),
     1),

    ((4, 2, 6),
     2),

    ((6, 1, 10),
     3),
]
for inp, exp in tests:
    res = s.maxValue(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
