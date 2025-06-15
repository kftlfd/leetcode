"""
Leetcode
2025-06-15
1432. Max Difference You Can Get From Changing an Integer
Medium
Topics
premium lock iconCompanies
Hint

You are given an integer num. You will apply the following steps to num two separate times:

    Pick a digit x (0 <= x <= 9).
    Pick another digit y (0 <= y <= 9). Note y can be equal to x.
    Replace all the occurrences of x in the decimal representation of num by y.

Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

 

Constraints:

    1 <= num <= 10^8


Hint 1
We need to get the max and min value after changing num and the answer is max - min.
Hint 2
Use brute force, try all possible changes and keep the minimum and maximum values.
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.62MB Beats 88.27%
    """

    def maxDiff(self, num: int) -> int:
        num_s = str(num)
        return self.get_max(num_s) - self.get_min(num_s)

    def get_max(self, num: str) -> int:
        out = num
        for c in num:
            if c != "9":
                out = out.replace(c, "9")
                break
        return int(out)

    def get_min(self, num: str) -> int:
        out = num
        first = num[0]
        for i, c in enumerate(num):
            if i == 0:
                if c != "1":
                    out = out.replace(c, "1")
                    break
            else:
                if c != first and c != "0":
                    out = out.replace(c, "0")
                    break
        return int(out)


class Solution1:
    """
    leetcode solution 1: Enumeration
    Runtime 9ms Beats 7.14%
    Memory 17.79MB Beats 58.67%
    """

    def maxDiff(self, num: int) -> int:
        def change(x, y):
            return str(num).replace(str(x), str(y))

        min_num = max_num = num
        for x in range(10):
            for y in range(10):
                res = change(x, y)
                # Check if there are leading zeros
                if res[0] != "0":
                    res_i = int(res)
                    min_num = min(min_num, res_i)
                    max_num = max(max_num, res_i)

        return max_num - min_num


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime 0ms Beats 100.00%
    Memory 17.91MB Beats 15.31%
    """

    def maxDiff(self, num: int) -> int:
        min_num, max_num = str(num), str(num)

        # Find a high position and replace it with 9.
        for digit in max_num:
            if digit != "9":
                max_num = max_num.replace(digit, "9")
                break

        # Replace the most significant bit with 1
        # Or find a high-order digit that is not equal to the highest digit and replace it with 0.
        for i, digit in enumerate(min_num):
            if i == 0:
                if digit != "1":
                    min_num = min_num.replace(digit, "1")
                    break
            else:
                if digit != "0" and digit != min_num[0]:
                    min_num = min_num.replace(digit, "0")
                    break

        return int(max_num) - int(min_num)
