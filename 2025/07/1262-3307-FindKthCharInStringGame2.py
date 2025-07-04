"""
Leetcode
2025-07-04
3307. Find the K-th Character in String Game II
Hard

Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k. You are also given an integer array operations, where operations[i] represents the type of the ith operation.

Now Bob will ask Alice to perform all operations in sequence:

    If operations[i] == 0, append a copy of word to itself.
    If operations[i] == 1, generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word after performing all the operations.

Note that the character 'z' can be changed to 'a' in the second type of operation.

 

Example 1:

Input: k = 5, operations = [0,0,0]

Output: "a"

Explanation:

Initially, word == "a". Alice performs the three operations as follows:

    Appends "a" to "a", word becomes "aa".
    Appends "aa" to "aa", word becomes "aaaa".
    Appends "aaaa" to "aaaa", word becomes "aaaaaaaa".

Example 2:

Input: k = 10, operations = [0,1,0,1]

Output: "b"

Explanation:

Initially, word == "a". Alice performs the four operations as follows:

    Appends "a" to "a", word becomes "aa".
    Appends "bb" to "aa", word becomes "aabb".
    Appends "aabb" to "aabb", word becomes "aabbaabb".
    Appends "bbccbbcc" to "aabbaabb", word becomes "aabbaabbbbccbbcc".

 

Constraints:

    1 <= k <= 10^14
    1 <= operations.length <= 100
    operations[i] is either 0 or 1.
    The input is generated such that word has at least k characters after all operations.


Hint 1
Try to replay the operations kth character was part of.
Hint 2
The kth character is only affected if it is present in the first half of the string.
"""

from typing import List


class Solution00:
    """
    Wrong Answer
    """

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word_len = 2 ** len(operations)
        shifts = 0

        for op in operations[::-1]:
            word_len //= 2

            if op == 1 and k > word_len:
                shifts += 1

            k //= 2

        return chr(ord("a") + (shifts % 26))


class Solution01:
    """
    Wrong Answer
    """

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word_len = 1 << len(operations)
        shifts = 0

        for op in operations[::-1]:
            word_len //= 2
            if k > word_len:
                k //= 2
                shifts += op == 1

        return chr(ord("a") + (shifts % 26))


class Solution02:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.83MB Beats 53.62%
    """

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word_len = 1 << len(operations)
        shifts = 0

        for op in operations[::-1]:
            word_len //= 2
            if k > word_len:
                k -= word_len
                shifts += op == 1

        return chr(ord("a") + (shifts % 26))


class Solution1:
    """
    leetcode solution 1: Iteration
    Runtime 1ms Beats 46.38%
    Memory 17.81MB Beats 53.62%
    """

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        The general idea of this problem is the same as that of "Find the K-th Character 
        in String Game I," with the only difference being that we need to determine 
        which operation the current k is located in.

        Let k = 2^t + a. If a == 0, then the current k is in the (t-1)-th operation; 
        if a != 0, then the current k is in the t-th operation.

        This conclusion can be easily derived by simulating with small amounts of data.

        After determining the number of operations corresponding to the current k, we can 
        decide whether to accumulate the answer using the operations array provided in the 
        problem. If operations[t] = 1, we perform the accumulation; otherwise, we do not.
        """

        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))


class Solution2:
    """
    leetcode solution 2: Mathematics
    Runtime 1ms Beats 46.38%
    Memory 17.77MB Beats 81.16%
    """

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        Change the way of thinking: if you start counting from the character after the original 
        string, reaching the k-th character is equivalent to moving forward k-1 characters.

        Write k-1 in binary. When the t-th bit is 1, it corresponds to shifting forward by 2^(t-1) 
        characters, which is equivalent to applying the (t-1)-th operation.

        Therefore, we only need to pay attention to the positions of the binary number representing 
        k-1 where the bit is 1. If the corresponding value in the operations array at that position 
        is 1, we add it to the answer.
        """

        ans = 0
        k -= 1
        for i in range(k.bit_length() - 1, -1, -1):
            if (k >> i) & 1:
                ans += operations[i]
        return chr(ord("a") + (ans % 26))
