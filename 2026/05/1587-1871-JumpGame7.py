"""
Leetcode
2026-05-25
1871. Jump Game VII
Medium

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

    i + minJump <= j <= min(i + maxJump, s.length - 1), and
    s[j] == '0'.

Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false

 

Constraints:

    2 <= s.length <= 10^5
    s[i] is either '0' or '1'.
    s[0] == '0'
    1 <= minJump <= maxJump < s.length

 
"""


from collections import deque


class Solution:
    """
    Time Limit Exceeded
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        q = deque([0])
        last_checked_idx = 0

        while q:
            cur = q.popleft()

            for j in range(max(last_checked_idx + 1, cur + minJump), min(n, cur + maxJump + 1)):
                if s[j] == "0":
                    if j == n - 1:
                        return True
                    q.append(j)
                    last_checked_idx = j

        return False


class Solution1:
    """
    leetcode solution: Dynamic Programming + Prefix Sum Optimization
    Runtime 223ms Beats 22.40%
    Memory 24.40MB Beats 18.48%
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        f, pre = [0] * n, [0] * n
        f[0] = 1

        # since we start dynamic programming from i=minJump, we need to precompute the prefix sums for the part [0, minJump)
        for i in range(minJump):
            pre[i] = 1

        for i in range(minJump, n):
            left, right = i - maxJump, i - minJump
            if s[i] == "0":
                total = pre[right] - (0 if left <= 0 else pre[left - 1])
                f[i] = int(total != 0)
            pre[i] = pre[i - 1] + f[i]

        return bool(f[n - 1])
