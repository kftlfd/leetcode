"""
Leetcode
2264. Largest 3-Same-Digit Number in String
EasyYou are given a string num representing a large integer. An integer is good if it meets the following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.

 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

 

Constraints:

    3 <= num.length <= 1000
    num only consists of digits.
2023-12-04


"""


class Solution:
    """
    Runtime: 41 ms, faster than 67.89% of Python3 online submissions for Largest 3-Same-Digit Number in String.
    Memory Usage: 16.4 MB, less than 24.76% of Python3 online submissions for Largest 3-Same-Digit Number in String.
    """
    
    def largestGoodInteger(self, num: str) -> str:
        digit = -1
        
        for i in range(2, len(num)):
            cur = num[i]
            if cur == num[i-1] and cur == num[i-2]:
                digit = max(digit, int(cur))
                
        return "" if digit == -1 else str(digit) * 3