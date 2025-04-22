"""
Leetcode
2025-04-22
2338. Count the Number of Ideal Arrays
Hard

You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

    Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
    Every arr[i] is divisible by arr[i - 1], for 0 < i < n.

Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.

Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays):
   - With no other distinct values (1 array): [1,1,1,1,1]
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.



Constraints:

    2 <= n <= 10^4
    1 <= maxValue <= 10^4


Hint 1
Notice that an ideal array is non-decreasing.
Hint 2
Consider an alternative problem: where an ideal array must also be strictly increasing. Can you use DP to solve it?
Hint 3
Will combinatorics help to get an answer from the alternative problem to the actual problem?
"""

MOD = 10**9 + 7
MAX_N = 10**4 + 10
MAX_P = 15  # 最多 15 个质因子

sieve = [0] * MAX_N  # 最小质因子

for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

ps = [[] for _ in range(MAX_N)]

for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        ps[i].append(cnt)

c = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]

c[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    c[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD


class Solution:
    """
    leetcode solution: Combinatorial Mathematics
    Runtime 22ms Beats 92.06%
    Memory 25.28MB Beats 44.44%
    """

    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = 0
        for num in range(1, maxValue + 1):
            mul = 1
            for prime in ps[num]:
                mul = mul * c[n + prime - 1][prime] % MOD
            ans = (ans + mul) % MOD
        return ans
