"""
Leetcode
2025-05-12
2094. Finding 3-Digit Even Numbers
Easy

You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

    The integer consists of the concatenation of three elements from digits in any arbitrary order.
    The integer does not have leading zeros.
    The integer is even.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

 

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.

Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 

Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.

 

Constraints:

    3 <= digits.length <= 100
    0 <= digits[i] <= 9


Hint 1
The range of possible answers includes all even numbers between 100 and 999 inclusive. Could you check each possible answer to see if it could be formed from the digits in the array?
"""

from typing import List


class Solution:
    """
    Runtime 23ms Beats 78.44%
    Memory 17.80MB Beats 65.57%
    """

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1

        ans = []

        for i in range(100, 1000):
            if i & 1 == 1:
                continue
            cnt2 = self.getCnt(i)
            if self.cntIsSubset(cnt, cnt2):
                ans.append(i)

        return ans

    def getCnt(self, num: int) -> List[int]:
        cnt = [0] * 10
        while num > 0:
            d = num % 10
            cnt[d] += 1
            num //= 10
        return cnt

    def cntIsSubset(self, cnt1: List[int], cnt2: List[int]) -> bool:
        for c1, c2 in zip(cnt1, cnt2):
            if c2 > c1:
                return False
        return True


class Solution1:
    """
    leetcode solution: Enumerate the Element Combinations in an Array
    Runtime 3226ms Beats 18.79%
    Memory 17.90MB Beats 65.57%
    """

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()  # Target even set
        n = len(digits)
        # Traverse the indices of three digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Determine whether it meets the condition of the target even number
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        # Converted to an array sorted in ascending order
        res = sorted(list(nums))
        return res
