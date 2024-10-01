"""
Leetcode
2024-10-01
1497. Check If Array Pairs Are Divisible by k
Medium

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).

Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

 

Constraints:

    arr.length == n
    1 <= n <= 10^5
    n is even.
    -109 <= arr[i] <= 10^9
    1 <= k <= 10^5

Hints:
- Keep an array of the frequencies of ((x % k) + k) % k for each x in arr.
- for each i in [0, k - 1] we need to check if freq[i] == freq[k - i]
- Take care of the case when i == k - i and when i == 0
"""

from typing import List


class Solution:
    """
    Runtime: 469 ms, faster than 88.48% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
    Memory Usage: 30.4 MB, less than 73.50% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
    """

    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = [0] * k

        for num in arr:
            mods[((num % k) + k) % k] += 1

        if mods[0] % 2 == 1:
            return False

        for i in range(1, (k // 2) + 1):
            if mods[i] != mods[k - i]:
                return False

        return True


class Solution2:
    """
    leetcode solution 2: Sorting and Two-Pointers
    Runtime: 540 ms, faster than 14.29% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
    Memory Usage: 30.3 MB, less than 73.50% of Python3 online submissions for Check If Array Pairs Are Divisible by k.
    """

    def canArrange(self, arr: List[int], k: int) -> bool:
        # Custom comparator to sort based on mod values.
        arr = sorted(arr, key=lambda x: (k + x % k) % k)

        # Assign the pairs with modulo 0 first.
        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] % k != 0:
                break
            if arr[start + 1] % k != 0:
                return False
            start = start + 2

        # Now, pick one element from the beginning and one element from the
        # end.
        while start < end:
            if (arr[start] + arr[end]) % k != 0:
                return False
            start += 1
            end -= 1

        return True


s = Solution()
tests = [
    (([-1, -1, -1, -1, 2, 2, -2, -2], 3),
     False),

    (([3, 8, 7, 2], 10),
     True),
]
for inp, exp in tests:
    res = s.canArrange(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
