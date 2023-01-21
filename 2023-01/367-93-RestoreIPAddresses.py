"""
Leetcode
93. Restore IP Addresses (medium)
2023-01-21

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""

from typing import List, Optional
from itertools import combinations


# https://leetcode.com/problems/restore-ip-addresses/solution/1767102
# Runtime: 39 ms, faster than 74.31% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 13.9 MB, less than 79.81% of Python3 online submissions for Restore IP Addresses.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ans = []
        l = len(s)
        if l < 4 or l > 12:
            return ans

        def leading_0(string):
            return string[0] == "0" and string != "0"

        def valid(part):
            return not leading_0(part) and int(part) <= 255

        def valid_ip(nums):
            return all(valid(part) for part in nums)

        for i, j, k in combinations(range(1, l), 3):
            ip = [s[:i], s[i:j], s[j:k], s[k:]]
            if valid_ip(ip):
                ans.append(".".join(ip))

        return ans


s = Solution()
tests = [
    ("25525511135",
     ["255.255.11.135", "255.255.111.35"]),

    ("0000",
     ["0.0.0.0"]),

    ("101023",
     ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
]
for inp, exp in tests:
    res = s.restoreIpAddresses(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
