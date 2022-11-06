"""
Leetcode
899. Orderly Queue (hard)
2022-11-06

You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

Example 1:
Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".

Example 2:
Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
"""

from typing import List, Optional


# leetcode solution
# Runtime: 67 ms, faster than 28.57% of Python3 online submissions for Orderly Queue.
# Memory Usage: 13.8 MB, less than 72.62% of Python3 online submissions for Orderly Queue.
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # If k = 1, only rotations of s are possible, and the answer is the lexicographically smallest rotation.
        # If k > 1, any permutation of s is possible, and the answer is the letters of s written in lexicographic order.
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))


s = Solution()
tests = [
    (("cba", 1),
     "acb"),

    (("baaca", 3),
     "aaabc"),
]
for inp, exp in tests:
    res = s.orderlyQueue(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
