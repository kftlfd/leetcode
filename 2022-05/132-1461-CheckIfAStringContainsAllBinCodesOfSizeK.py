"""
Leetcode
1461. Check If a String Contains All Binary Codes of Size K (medium)
2022-05-31

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
"""



# leetcode solution - set
# Runtime: 352 ms, faster than 89.82% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Memory Usage: 27.1 MB, less than 51.77% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k
       


s = Solution()
tests = [
    ["00110110", 2],
    ["0110", 1],
    ["0110", 2]
]
for t in tests:
    print(t)
    print(s.hasAllCodes(t[0], t[1]))
    print()
