"""
Leetcode
2026-03-30
2840. Check if Strings Can be Made Equal With Operations II
Medium

You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

    Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.

Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.

 

Constraints:

    n == s1.length == s2.length
    1 <= n <= 10^5
    s1 and s2 consist only of lowercase English letters.


"""


from collections import Counter


class Solution:
    """
    Runtime 51ms Beats 83.58%
    Memory 20.06MB Beats 82.09%
    """

    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_even = Counter(s1[::2])
        s2_even = Counter(s2[::2])
        if s1_even != s2_even:
            return False

        s1_odd = Counter(s1[1::2])
        s2_odd = Counter(s2[1::2])
        return s1_odd == s2_odd


class Solution1:
    """
    leetcode solution
    Runtime 45ms Beats 96.27%
    Memory 20.17MB Beats 68.66%
    """

    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
