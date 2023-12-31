"""
Leetcode

2022-10-18


"""

from typing import List, Optional


# Runtime: 91 ms, faster than 44.51% of Python3 online submissions for Count and Say.
# Memory Usage: 14.2 MB, less than 7.99% of Python3 online submissions for Count and Say.
class Solution:

    memo = {1: "1", 2: "11"}
    last = 2

    def helper(self, n: int) -> str:
        prev = self.memo[n-1]
        seq = []
        for i, d in enumerate(prev):
            if i == 0 or seq[-1][1] != d:
                seq.append([1, d])
            else:
                seq[-1][0] += 1
        seq = [str(i) for sublist in seq for i in sublist]
        return "".join(seq)

    def countAndSay(self, n: int) -> str:

        if n in self.memo:
            return self.memo[n]

        for i in range(self.last + 1, n + 1):
            self.memo[i] = self.helper(i)

        self.last = n
        return self.memo[n]


s = Solution()
tests = [
    1, 4
]
for t in tests:
    print(t)
    print(s.countAndSay(t))
    print()
