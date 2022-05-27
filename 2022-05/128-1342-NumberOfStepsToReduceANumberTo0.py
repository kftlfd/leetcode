"""
Leetcode
1342. Number of Steps to Reduce a Number to Zero (easy)
2022-05-27

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""



# try 1 - simulation
# Runtime: 42 ms, faster than 51.62% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.9 MB, less than 53.50% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps



# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/502809/just-count-number-of-0-and-1-in-binary
# Runtime: 38 ms, faster than 64.36% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 53.50% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
class Solution1:
    def numberOfSteps(self, num: int) -> int:
        # if not num: return 0
        # steps = 0
        # while num:
        #     if num & 1 == 1:
        #         steps += 2
        #     else:
        #         steps += 1
        #     num >>= 1
        # return steps - 1

        # https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/502809/just-count-number-of-0-and-1-in-binary/463525
        if not num: return 0
        steps = 0
        while num:
            steps += (num & 1) + 1
            num >>= 1
        return steps - 1        



s = Solution1()
tests = [14, 8, 123, 0]
for t in tests:
    print(t)
    print(s.numberOfSteps(t))
    print()
