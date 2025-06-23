"""
Leetcode
2025-06-23
2081. Sum of k-Mirror Numbers
Hard

A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

    For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
    On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.

Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

 

Example 1:

Input: k = 2, n = 5
Output: 25
Explanation:
The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
  base-10    base-2
    1          1
    3          11
    5          101
    7          111
    9          1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25. 

Example 2:

Input: k = 3, n = 7
Output: 499
Explanation:
The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
  base-10    base-3
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.

Example 3:

Input: k = 7, n = 17
Output: 20379000
Explanation: The 17 smallest 7-mirror numbers are:
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596

 

Constraints:

    2 <= k <= 9
    1 <= n <= 30


Hint 1
Since we need to reduce search space, instead of checking if every number is a palindrome in base-10, can we try to "generate" the palindromic numbers?
Hint 2
If you are provided with a d digit number, how can you generate a palindrome with 2*d or 2*d - 1 digit?
Hint 3
Try brute-forcing and checking if the palindrome you generated is a "k-Mirror" number.
"""

from typing import List


class Solution:
    """
    Runtime 3900ms Beats 34.84%
    Memory 17.84MB Beats 51.61%
    """

    def kMirror(self, k: int, n: int) -> int:
        ans = 0
        count = 0
        for num_list in self.get_palindromic_ints():
            num = self.int_from_list(num_list)
            if self.is_palindromic(self.int_to_base(num, k)):
                ans += num
                count += 1
                if count >= n:
                    break
        return ans

    def get_palindromic_ints(self):
        cur_len = 0
        while True:
            cur_len += 1

            if cur_len == 1:
                for i in range(1, 10):
                    yield [i]

            elif cur_len % 2 == 0:
                num = int("1" + "0" * (cur_len // 2 - 1))
                for i in range(num, num * 10):
                    arr = self.int_to_base(i, 10)
                    yield arr + arr[::-1]

            else:
                num = int("1" + "0" * (cur_len // 2 - 1))
                for i in range(num, num * 10):
                    arr = self.int_to_base(i, 10)
                    for j in range(10):
                        yield arr + [j] + arr[::-1]

    def int_from_list(self, int_list: List[int]) -> int:
        cur = 0
        for num in int_list:
            cur = cur * 10 + num
        return cur

    def is_palindromic(self, int_list: List[int]) -> bool:
        for i in range(len(int_list) // 2):
            if int_list[i] != int_list[-i-1]:
                return False
        return True

    def int_to_base(self, num: int, base: int) -> List[int]:
        digits = []
        while num > 0:
            digits.insert(0, num % base)
            num //= base
        return digits


class Solution1:
    """
    leetcode solution 1: Binary Search
    Runtime 2349ms Beats 69.03%
    Memory 17.79MB Beats 74.19%
    """

    def kMirror(self, k: int, n: int) -> int:
        def isPalindrome(x: int) -> bool:
            digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]

        left, cnt, ans = 1, 0, 0

        while cnt < n:
            right = left * 10
            # op = 0 indicates enumerating odd-length palindromes
            # op = 1 indicates enumerating even-length palindromes
            for op in [0, 1]:
                # enumerate i'
                for i in range(left, right):
                    if cnt == n:
                        break

                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        cnt += 1
                        ans += combined
            left = right

        return ans


class Solution2:
    """
    leetcode solution 2: Preprocessing (lol)
    Runtime 0ms Beats 100.00%
    Memory 17.80MB Beats 74.19%
    """

    ANS = [
        [
            1,
            3,
            5,
            7,
            9,
            33,
            99,
            313,
            585,
            717,
            7447,
            9009,
            15351,
            32223,
            39993,
            53235,
            53835,
            73737,
            585585,
            1758571,
            1934391,
            1979791,
            3129213,
            5071705,
            5259525,
            5841485,
            13500531,
            719848917,
            910373019,
            939474939,
        ],
        [
            1,
            2,
            4,
            8,
            121,
            151,
            212,
            242,
            484,
            656,
            757,
            29092,
            48884,
            74647,
            75457,
            76267,
            92929,
            93739,
            848848,
            1521251,
            2985892,
            4022204,
            4219124,
            4251524,
            4287824,
            5737375,
            7875787,
            7949497,
            27711772,
            83155138,
        ],
        [
            1,
            2,
            3,
            5,
            55,
            373,
            393,
            666,
            787,
            939,
            7997,
            53235,
            55255,
            55655,
            57675,
            506605,
            1801081,
            2215122,
            3826283,
            3866683,
            5051505,
            5226225,
            5259525,
            5297925,
            5614165,
            5679765,
            53822835,
            623010326,
            954656459,
            51717171715,
        ],
        [
            1,
            2,
            3,
            4,
            6,
            88,
            252,
            282,
            626,
            676,
            1221,
            15751,
            18881,
            10088001,
            10400401,
            27711772,
            30322303,
            47633674,
            65977956,
            808656808,
            831333138,
            831868138,
            836131638,
            836181638,
            2512882152,
            2596886952,
            2893553982,
            6761551676,
            12114741121,
            12185058121,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            7,
            55,
            111,
            141,
            191,
            343,
            434,
            777,
            868,
            1441,
            7667,
            7777,
            22022,
            39893,
            74647,
            168861,
            808808,
            909909,
            1867681,
            3097903,
            4232324,
            4265624,
            4298924,
            4516154,
            4565654,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            8,
            121,
            171,
            242,
            292,
            16561,
            65656,
            2137312,
            4602064,
            6597956,
            6958596,
            9470749,
            61255216,
            230474032,
            466828664,
            485494584,
            638828836,
            657494756,
            858474858,
            25699499652,
            40130703104,
            45862226854,
            61454945416,
            64454545446,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            9,
            121,
            292,
            333,
            373,
            414,
            585,
            3663,
            8778,
            13131,
            13331,
            26462,
            26662,
            30103,
            30303,
            207702,
            628826,
            660066,
            1496941,
            1935391,
            1970791,
            4198914,
            55366355,
        ],
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            191,
            282,
            373,
            464,
            555,
            646,
            656,
            6886,
            25752,
            27472,
            42324,
            50605,
            626626,
            1540451,
            1713171,
            1721271,
            1828281,
            1877781,
            1885881,
            2401042,
            2434342,
            2442442,
        ],
    ]

    def kMirror(self, k: int, n: int) -> int:
        return sum(self.ANS[k - 2][:n])
