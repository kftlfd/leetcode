"""
Leetcode
1750. Minimum Length of String After Deleting Similar Ends
Medium
2024-03-05

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

    Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    The prefix and the suffix should not intersect at any index.
    The characters from the prefix and suffix must be the same.
    Delete both the prefix and the suffix.

Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

 

Constraints:

    1 <= s.length <= 105
    s only consists of characters 'a', 'b', and 'c'.

Hints:
- If both ends have distinct characters, no more operations can be made. Otherwise, the only operation is to remove all of the same characters from both ends. We will do this as many times as we can.
- Note that if the length is equal 1 the answer is 1
"""


class Solution:
    """
    Runtime: 81 ms, faster than 31.75% of Python3 online submissions for Minimum Length of String After Deleting Similar Ends.
    Memory Usage: 17.2 MB, less than 98.58% of Python3 online submissions for Minimum Length of String After Deleting Similar Ends.
    """

    def minimumLength(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left = 0
        right = len(s) - 1

        while s[left] == s[right] and left < right:

            while left < len(s) - 1 and s[left + 1] == s[left] and left + 1 < right:
                left += 1

            while right > 0 and s[right - 1] == s[right] and right - 1 > left:
                right -= 1

            left += 1
            right -= 1

        return right - left + 1


class Solution1:
    """
    leetcode solution 1: Two Pointers
    Runtime: 59 ms, faster than 91.47% of Python3 online submissions for Minimum Length of String After Deleting Similar Ends.
    Memory Usage: 17.4 MB, less than 53.55% of Python3 online submissions for Minimum Length of String After Deleting Similar Ends.
    """

    def minimumLength(self, s: str) -> int:
        begin = 0
        end = len(s) - 1

        # Delete similar ends until the ends differ or they meet in the middle
        while begin < end and s[begin] == s[end]:
            c = s[begin]

            # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

        # Return the number of remaining characters
        return end - begin + 1


class Solution2:
    """
    leetcode solution 2: Tail Recursion
    Runtime: 79 ms, faster than 34.60% of Python3 online submissions for Minimum Length of String After Deleting Similar Ends.
    Memory Usage: 27.7 MB, less than 5.21% of Python3 online submissions for Minimum Length of String After Deleting Similar Ends.
    """

    def minimumLength(self, s: str) -> int:
        return self.delete_similar_ends(s, 0, len(s) - 1)

    # Deletes similar ends and returns remaining length
    def delete_similar_ends(self, s: str, begin: int, end: int) -> int:
        # The ends differ or meet in the middle
        if begin >= end or s[begin] != s[end]:
            return end - begin + 1
        else:
            c = s[begin]

            # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

            return self.delete_similar_ends(s, begin, end)
