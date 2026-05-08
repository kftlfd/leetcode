"""
Leetcode
2026-05-08
3629. Minimum Jumps to Reach End via Prime Teleportation
Medium

You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

    Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
    Prime Teleportation: If nums[i] is a p, you may instantly jump to any index j != i such that nums[j] % p == 0.

Return the minimum number of jumps required to reach index n - 1.

 

Example 1:

Input: nums = [1,2,4,6]

Output: 2

Explanation:

One optimal sequence of jumps is:

    Start at index i = 0. Take an adjacent step to index 1.
    At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.

Thus, the answer is 2.

Example 2:

Input: nums = [2,3,4,7,9]

Output: 2

Explanation:

One optimal sequence of jumps is:

    Start at index i = 0. Take an adjacent step to index i = 1.
    At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.

Thus, the answer is 2.

Example 3:

Input: nums = [4,6,5,8]

Output: 3

Explanation:

    Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.

 

Constraints:

    1 <= n == nums.length <= 10^5
    1 <= nums[i] <= 10^6


Hint 1
Use a breadth-first search.
Hint 2
Precompute prime factors of each nums[i] via a sieve, and build a bucket bucket[p] mapping each prime p to all indices j with nums[j] % p == 0.
Hint 3
During the BFS, when at index i, enqueue its adjacent steps (i+1 and i-1) and all indices in bucket[p] for each prime p dividing nums[i], then clear bucket[p] so each prime's bucket is visited only once.
"""


from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def minJumps(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_num = max(nums)
        primes = self._get_primes(max_num)
        prime_factors: dict[int, List[int]] = {}
        bucket: dict[int, List[int]] = defaultdict(list)

        for i, num in enumerate(nums):
            if num not in prime_factors:
                prime_factors[num] = self._get_prime_factors(num, primes)
            for p in prime_factors[num]:
                bucket[p].append(i)

        return self._bfs(nums, bucket)

    def _bfs(self, nums: List[int], bucket: dict[int, List[int]]):
        seen = {0}
        q = deque([0])
        n = len(nums)
        steps = 0

        while q:
            steps += 1

            for _ in range(len(q)):
                cur = q.popleft()

                if cur > 0 and cur - 1 not in seen:
                    seen.add(cur - 1)
                    q.append(cur - 1)

                if cur + 1 < n and cur + 1 not in seen:
                    if cur + 1 == n - 1:
                        return steps
                    seen.add(cur + 1)
                    q.append(cur + 1)

                for nxt in bucket[nums[cur]]:
                    if nxt == n - 1:
                        return steps
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)

        return steps

    def _get_primes(self, max_num: int) -> List[bool]:
        primes = [True] * (max_num + 1)
        primes[0] = False
        primes[1] = False
        for num in range(2, max_num // 2 + 1):
            for mult in range(num + num, max_num + 1, num):
                primes[mult] = False
        return primes

    def _get_prime_factors(self, num: int, primes: List[bool]) -> List[int]:
        return [f for f, is_prime in enumerate(primes[:num+1]) if is_prime and num % f == 0]


class Solution1:
    """
    leetcode solution 1: Reversed Breadth-First Search
    Time Limit Exceeded
    """

    def minJumps(self, nums: List[int]) -> int:
        factors = self._get_factors()
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            if len(factors[a]) == 1:
                edges[a].append(i)
        res = 0
        seen = [False] * n
        seen[-1] = True
        q = [n - 1]
        while True:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1

    def _get_factors(self):
        MX = 1_000_001
        factors = [[] for _ in range(MX)]
        for i in range(2, MX):
            if not factors[i]:
                for j in range(i, MX, i):
                    factors[j].append(i)
        return factors


def create_s2_factors():
    MX = 1_000_001
    factors = [[] for _ in range(MX)]
    for i in range(2, MX):
        if not factors[i]:
            for j in range(i, MX, i):
                factors[j].append(i)
    return factors


s2_factors = create_s2_factors()


class Solution2:
    """
    leetcode solution 2: Forward Breadth-First Search
    Runtime 725ms Beats 93.71%
    Memory 147.34MB Beats 16.03%
    """

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        factors = s2_factors
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            for p in factors[a]:
                edges[p].append(i)
        res = 0
        seen = [False] * n
        seen[0] = True
        q = [0]
        while True:
            q2 = []
            for i in q:
                if i == n - 1:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                if len(factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1
