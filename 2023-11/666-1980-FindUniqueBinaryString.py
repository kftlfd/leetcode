"""
Leetcode
1980. Find Unique Binary String (medium)
2023-11-16

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

 

Constraints:

    n == nums.length
    1 <= n <= 16
    nums[i].length == n
    nums[i] is either '0' or '1'.
    All the strings of nums are unique.

Hints:
- We can convert the given strings into base 10 integers.
- Can we use recursion to generate all possible strings?
"""

from typing import List


class Solution:
    """
    Runtime: 48 ms, faster than 27.53% of Python3 online submissions for Find Unique Binary String.
    Memory Usage: 16.4 MB, less than 27.31% of Python3 online submissions for Find Unique Binary String.
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strings = set(nums)
        n = len(nums[0])
        formatter = f"0{n}b"

        for i in range(1 << n):  # 2**n
            bin_str = format(i, formatter)
            if bin_str not in strings:
                return bin_str


class Solution1:
    """
    leetcode solution 1: Recursively Generate All Strings
    Runtime: 44 ms, faster than 46.90% of Python3 online submissions for Find Unique Binary String.
    Memory Usage: 16.5 MB, less than 27.31% of Python3 online submissions for Find Unique Binary String.
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr

                return ""

            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero

            return generate(curr + "1")

        n = len(nums)
        nums = set(nums)
        return generate("")


class Solution2:
    """
    leetcode solution 2: Iterate Over Integer Equivalents
    Runtime: 44 ms, faster than 46.90% of Python3 online submissions for Find Unique Binary String.
    Memory Usage: 16.3 MB, less than 42.98% of Python3 online submissions for Find Unique Binary String.
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                return format(num, f"0{n}b")

        return ""


class Solution4:
    """
    leetcode solution 4: Cantor's Diagonal Argument
    Runtime: 45 ms, faster than 38.96% of Python3 online submissions for Find Unique Binary String.
    Memory Usage: 16.3 MB, less than 66.27% of Python3 online submissions for Find Unique Binary String.
    """

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)
