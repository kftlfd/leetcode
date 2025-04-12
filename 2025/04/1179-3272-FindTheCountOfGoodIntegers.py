"""
Leetcode
2025-04-12
3272. Find the Count of Good Integers
Hard

You are given two positive integers n and k.

An integer x is called k-palindromic if:

    x is a 

    .
    x is divisible by k.

An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

Return the count of good integers containing n digits.

Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

Example 1:

Input: n = 3, k = 5

Output: 27

Explanation:

Some of the good integers are:

    551 because it can be rearranged to form 515.
    525 because it is already k-palindromic.

Example 2:

Input: n = 1, k = 4

Output: 2

Explanation:

The two good integers are 4 and 8.

Example 3:

Input: n = 5, k = 6

Output: 2468

 

Constraints:

    1 <= n <= 10
    1 <= k <= 9


Hint 1
How to generate all K-palindromic strings of length n? Do we need to go through all n digits?
Hint 2
Use permutations to calculate the number of possible rearrangements.
"""

from math import factorial


class Solution:
    """
    leetcode solution: Enumeration + Permutations and Combinations
    Runtime 854ms Beats 98.39%
    Memory 19.10MB Beats 61.29%
    """

    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        # Enumerate the number of palindrome numbers of n digits
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            # If the current palindrome number is a k-palindromic integer
            if palindromicInteger % k == 0:
                sorted_s = "".join(sorted(s))
                dictionary.add(sorted_s)

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            # Calculate permutations and combinations
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            ans += tot

        return ans
