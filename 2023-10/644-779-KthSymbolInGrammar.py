"""
Leetcode
779. K-th Symbol in Grammar (medium)
2023-10-25

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01

Example 3:

Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01

 

Constraints:

    1 <= n <= 30
    1 <= k <= 2^(n - 1)
"""


class Solution:
    """
    Runtime: 42 ms, faster than 27.32% of Python3 online submissions for K-th Symbol in Grammar.
    Memory Usage: 16.2 MB, less than 79.64% of Python3 online submissions for K-th Symbol in Grammar.
    """

    def kthGrammar(self, n: int, k: int) -> int:

        def get(row, position):
            if row == 0:
                return 0
            if row == 1:
                return position

            prev = get(row - 1, position // 2)

            return (prev + position) % 2

        return get(n - 1, k - 1)


class Solution1:
    """
    leetcode solution 1: Binary Tree Traversal
    Runtime: 32 ms, faster than 90.08% of Python3 online submissions for K-th Symbol in Grammar.
    Memory Usage: 16.4 MB, less than 17.91% of Python3 online submissions for K-th Symbol in Grammar.
    """

    def kthGrammar(self, n: int, k: int) -> int:
        return self.depthFirstSearch(n, k, 0)

    def depthFirstSearch(self, n: int, k: int, rootVal: int) -> int:
        if n == 1:
            return rootVal

        totalNodes = 2 ** (n - 1)

        # Target node will be present in the right half sub-tree of the current root node.
        if k > (totalNodes / 2):
            nextRootVal = 1 if rootVal == 0 else 0
            return self.depthFirstSearch(n - 1, k - (totalNodes / 2), nextRootVal)
        # Otherwise, the target node is in the left sub-tree of the current root node.
        else:
            nextRootVal = 0 if rootVal == 0 else 1
            return self.depthFirstSearch(n - 1, k, nextRootVal)


class Solution2:
    """
    leetcode solution 2: Normal Recursion
    Runtime: 36 ms, faster than 73.58% of Python3 online submissions for K-th Symbol in Grammar.
    Memory Usage: 16.3 MB, less than 50.00% of Python3 online submissions for K-th Symbol in Grammar.
    """

    def kthGrammar(self, n: int, k: int) -> int:
        return self.recursion(n, k)

    def recursion(self, n: int, k: int) -> int:
        # First row will only have one symbol '0'.
        if n == 1:
            return 0

        total_elements = 2 ** (n - 1)
        half_elements = total_elements // 2

        # If the target is present in the right half, we switch to the respective left half symbol.
        if k > half_elements:
            return 1 - self.recursion(n, k - half_elements)

        # Otherwise, we switch to the previous row.
        return self.recursion(n - 1, k)


class Solution3:
    """
    leetcode solution 3: Recursion to Iteration
    Runtime: 43 ms, faster than 21.91% of Python3 online submissions for K-th Symbol in Grammar.
    Memory Usage: 16.4 MB, less than 17.91% of Python3 online submissions for K-th Symbol in Grammar.
    """

    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # We assume the symbol at the target position is '1'.
        symbol = 1

        for curr_row in range(n, 1, -1):
            total_elements = 2 ** (curr_row - 1)
            half_elements = total_elements // 2

            # If 'k' lies in the right half symbol, then we flip over to the respective left half symbol.
            if k > half_elements:
                # Flip the symbol.
                symbol = 1 - symbol
                # Change the position after flipping.
                k -= half_elements

        # We reached the 1st row; if the symbol is not '0', we started with the wrong symbol.
        if symbol != 0:
            # Thus, the start symbol was '0', not '1'.
            return 0

        # The start symbol was indeed what we started with, a '1'.
        return 1


class Solution4:
    """
    leetcode solution 4: Math
    Runtime: 28 ms, faster than 96.91% of Python3 online submissions for K-th Symbol in Grammar.
    Memory Usage: 16.2 MB, less than 50.00% of Python3 online submissions for K-th Symbol in Grammar.
    """

    def kthGrammar(self, n: int, k: int) -> int:
        count = bin(k - 1).count('1')
        return 0 if count % 2 == 0 else 1


s = Solution()
tests = [
    ((1, 1),
     0),

    ((2, 1),
        0),

    ((2, 2),
        1),
]
for inp, exp in tests:
    res = s.kthGrammar(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
