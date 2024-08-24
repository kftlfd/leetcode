"""
Leetcode
564. Find the Closest Palindrome
Hard
2024-08-24

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"

Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.

 

Constraints:

    1 <= n.length <= 18
    n consists of only digits.
    n does not have leading zeros.
    n is representing an integer in the range [1, 10^18 - 1].

Hints:
- Will brute force work for this problem? Think of something else.
- Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?
- Do we have to consider only left half or right half of the string or both?
- Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?
"""


class Solution1:
    """
    leetcode solution 1: Find Previous and Next Palindromes
    Runtime: 35 ms, faster than 63.70% of Python3 online submissions for Find the Closest Palindrome.
    Memory Usage: 16.6 MB, less than 28.21% of Python3 online submissions for Find the Closest Palindrome.
    """

    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2
        first_half = int(n[: i + 1])

        '''
        Generate possible palindromic candidates:
        1. Create a palindrome by mirroring the first half.
        2. Create a palindrome by mirroring the first half incremented by 1.
        3. Create a palindrome by mirroring the first half decremented by 1.
        4. Handle edge cases by considering palindromes of the form 999... 
           and 100...001 (smallest and largest n-digit palindromes).
        '''

        possibilities = []
        possibilities.append(
            self.half_to_palindrome(first_half, len_n % 2 == 0)
        )
        possibilities.append(
            self.half_to_palindrome(first_half + 1, len_n % 2 == 0)
        )
        possibilities.append(
            self.half_to_palindrome(first_half - 1, len_n % 2 == 0)
        )
        possibilities.append(10 ** (len_n - 1) - 1)
        possibilities.append(10**len_n + 1)

        diff = float("inf")
        res = 0
        nl = int(n)
        for cand in possibilities:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(res, cand)
        return str(res)

    def half_to_palindrome(self, left: int, even: bool) -> int:
        res = left
        if not even:
            left = left // 10
        while left > 0:
            res = res * 10 + left % 10
            left //= 10
        return res


class Solution2:
    """
    leetcode solution 2: Binary Search
    Runtime: 53 ms, faster than 6.61% of Python3 online submissions for Find the Closest Palindrome.
    Memory Usage: 16.6 MB, less than 68.02% of Python3 online submissions for Find the Closest Palindrome.
    """

    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        a = self.next_palindrome(num)
        b = self.previous_palindrome(num)
        if abs(a - num) <= abs(b - num):
            return str(a)
        return str(b)

    def convert(self, num: int) -> int:
        s = str(num)
        n = len(s)
        l, r = (n - 1) // 2, n // 2
        s_list = list(s)
        while l >= 0:
            s_list[r] = s_list[l]
            r += 1
            l -= 1
        return int("".join(s_list))

    def next_palindrome(self, num: int) -> int:
        left, right = 0, num
        ans = float("-inf")
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin < num:
                ans = palin
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def previous_palindrome(self, num: int) -> int:
        left, right = num, int(1e18)
        ans = float("-inf")
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin > num:
                ans = palin
                right = mid - 1
            else:
                left = mid + 1
        return ans
