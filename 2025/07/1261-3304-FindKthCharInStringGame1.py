"""
Leetcode
2025-07-03
3304. Find the K-th Character in String Game I
Easy

Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

    Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.

For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character 'z' can be changed to 'a' in the operation.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

    Generated string is "b", word becomes "ab".
    Generated string is "bc", word becomes "abbc".
    Generated string is "bccd", word becomes "abbcbccd".

Example 2:

Input: k = 10

Output: "c"

 

Constraints:

    1 <= k <= 500


Hint 1
The constraints are small. Construct the string by simulating the operations.
"""

from collections import deque


class Solution:
    """
    Runtime 3ms Beats 85.63%
    Memory 17.96MB Beats 17.19%
    """

    def kthCharacter(self, k: int) -> str:
        q = deque([0])

        while len(q) < k:
            for i in range(min(len(q), k - len(q))):
                q.append((q[i] + 1) % 26)

        return chr(q[k - 1] + 97)


class Solution1:
    """
    leetcode solution: Iteration
    Runtime 0ms Beats 100.00%
    Memory 17.88MB Beats 39.50%
    """

    def kthCharacter(self, k: int) -> str:
        """
        Each character in the appended half is formed by applying a "+1 modulo 26" operation on 
        the corresponding character in the original string.

        Our goal is to find the character at the k-th position. To do this, we ask: which character 
        in the previous version of the string (let's call this position k') contributed to the 
        character at position k?

        Let k=2t+a.
            If a==0, then k lies in the (t-1)-th operation, and we set k' = k - 2^(t-1).
            If a!=0, then k lies in the t-th operation, and we set k' = k - 2^t = a.

        By iterating this process, we eventually reduce k' to 1, which corresponds to the 0-th 
        operation where the character is "a".

        Each iteration represents a single "+1" transformation, so we only need to count how many 
        such steps are taken.

        Since the constraint is 1≤k≤500, we don't need to worry about performing modulus 26 
        operations explicitly.
        """

        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            ans += 1
        return chr(ord("a") + ans)


class Solution2:
    """
    https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/editorial/comments/3060382/
    Runtime 2ms Beats 86.13%
    Memory 17.89MB Beats 39.50%
    """

    def kthCharacter(self, k: int) -> str:
        """
        Number of times a character is shifted is equal to the number of 1s in k - 1's binary 
        representation as each operation double length of string. The original part remains as 
        it is and new part added have the char shifted by 1. So, at Kth position - required 
        char is number of 1s in binary representation of (k - 1).

        e.g. k = 5, k - 1 = 4 (0100) gives b
        a -> ab -> abbc -> abbcbccd
        The fifth char is b
        """

        return chr(ord("a") + (k - 1).bit_count())
