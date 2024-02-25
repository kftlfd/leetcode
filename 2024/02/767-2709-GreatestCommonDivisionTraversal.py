"""
Leetcode
2709. Greatest Common Divisor Traversal
Hard
2024-02-25

You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

 

Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.

Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.

Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 105


"""

from collections import deque
from typing import List
from math import gcd


class Solution:
    """
    Time Limit Exceeded
    918 / 925 test cases passed.
    """

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        nums_left = set(nums)

        if len(nums_left) == 1:
            return self.gcd(nums[0], nums[0]) > 1

        q = deque([nums[0]])

        while q:
            cur = q.popleft()
            if cur in nums_left:
                nums_left.remove(cur)

            paths = []

            if not nums_left:
                return True

            for next_num in nums_left:
                if self.gcd(cur, next_num) > 1:
                    paths.append(next_num)

            if not paths and not q:
                return False

            for next_num in paths:
                nums_left.remove(next_num)
                q.append(next_num)

    def gcd(self, a: int, b: int) -> int:
        return gcd(a, b)


class Solution1:
    """
    Wrong answer
    """

    primes = [2, 3, 5, 7, 11, 13]

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        nums_left = set(nums)

        if len(nums_left) == 1:
            num = nums[0]
            return num > 1 and self.check_gcd(num, num)

        q = deque([nums[0]])

        while q:
            cur = q.popleft()
            if cur in nums_left:
                nums_left.remove(cur)

            paths = []

            if not nums_left:
                return True

            for next_num in nums_left:
                if self.check_gcd(cur, next_num):
                    paths.append(next_num)

            if not paths and not q:
                return False

            for next_num in paths:
                nums_left.remove(next_num)
                q.append(next_num)

    def check_gcd(self, a: int, b: int) -> int:
        """check that gcd(a,b) is > 1"""

        min_num, max_num = a, b
        if b < a:
            min_num, max_num = b, a

        min_num_half = min_num // 2
        self.gen_primes(min_num)
        f_min = float(min_num)
        f_max = float(max_num)

        # check divisors until min_num_half
        i = 0
        divisor = self.primes[i]
        while divisor <= min_num_half:
            if (f_min / divisor) % 1 == 0 and (f_max / divisor) % 1 == 0:
                return True
            i += 1
            divisor = self.primes[i]

        # check min_num as divisor
        if (f_max / min_num) % 1 == 0:
            return True

        return False

    def gen_primes(self, up_to: int):
        """
        generate primes
        https://stackoverflow.com/a/29813300
        """

        nextPrime = self.primes[-1] + 2

        while nextPrime <= up_to:
            isPrime = True
            i = 0
            squareRoot = int(nextPrime ** .5)

            while self.primes[i] <= squareRoot:
                if nextPrime % self.primes[i] == 0:
                    isPrime = False
                i += 1

            if isPrime:
                self.primes.append(nextPrime)

            nextPrime += 2


class Solution2:
    """
    leetcode solution: Creating a graph with dummy nodes and edges
    Time Limit Exceeded
    767 / 925 test cases passed.
    """

    class DSU:

        def __init__(self, n: int):
            self.dsu = list(range((n + 1) + 1))
            self.size = [1] * (n + 1)

        def find(self, x: int) -> int:
            if self.dsu[x] == x:
                return x
            self.dsu[x] = self.find(self.dsu[x])
            return self.dsu[x]

        def merge(self, x: int, y: int):
            fx = self.find(x)
            fy = self.find(y)
            if (fx == fy):
                return

            if self.size[fx] > self.size[fy]:
                fx, fy = fy, fx

            self.dsu[fx] = fy
            self.size[fy] += self.size[fx]

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        MAX = 10**5
        n = len(nums)
        has = [False] * (MAX + 1)
        for x in nums:
            has[x] = True

        # edge cases
        if n == 1:
            return True
        if has[1]:
            return False

        # general solution
        sieve = [0] * (MAX + 1)
        for d in range(2, MAX + 1):
            if sieve[d] == 0:
                for v in range(d, MAX + 1, d):
                    sieve[v] = d

        union = self.DSU(2 * MAX + 1)
        for x in nums:
            val = x
            while val > 1:
                prime = sieve[val]
                root = prime + MAX
                if union.find(root) != union.find(x):
                    union.merge(root, x)
                while val % prime == 0:
                    val //= prime

        cnt = 0
        for i in range(2, MAX + 1):
            if has[i] and union.find(i) == i:
                cnt += 1

        return cnt == 1


class Solution3:
    """
    https://leetcode.com/problems/greatest-common-divisor-traversal/discuss/3568567/Union-Find-in-C++-Java-and-Python
    Runtime: 5156 ms, faster than 34.38% of Python3 online submissions for Greatest Common Divisor Traversal.
    Memory Usage: 35.5 MB, less than 18.75% of Python3 online submissions for Greatest Common Divisor Traversal.
    """

    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        n = len(nums)
        if n == 1:
            return True
        f = [_ for _ in range(0, n)]
        num = [1] * n

        def getf(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = getf(f[x])
            return f[x]

        def merge(x: int, y: int):
            x, y = getf(x), getf(y)
            if x == y:
                return
            if num[x] < num[y]:
                x, y = y, x
            f[y] = x
            num[x] += num[y]

        have = {}
        for i in range(0, n):
            x = nums[i]
            if x == 1:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    if d in have:
                        merge(i, have[d])
                    else:
                        have[d] = i
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                if x in have:
                    merge(i, have[x])
                else:
                    have[x] = i
        return num[getf(0)] == n


s = Solution2()
tests = [
    ([1],
     True),

    ([1, 1],
     False),

    ([2, 3, 6],
     True),

    ([3, 9, 5],
     False),

    ([4, 3, 12, 8],
     True),

    ([42, 40, 45, 42, 50, 33, 30, 45, 33, 45, 30, 36, 44, 1, 21, 10, 40, 42, 42],
     False),
]
for inp, exp in tests:
    res = s.canTraverseAllPairs(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
