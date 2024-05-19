"""
Leetcode
3068. Find the Maximum Sum of Node Values
Hard
2024-05-19

There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

    Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
        nums[u] = nums[u] XOR k
        nums[v] = nums[v] XOR k

Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.

 

Example 1:

Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
Output: 6
Explanation: Alice can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.

Example 2:

Input: nums = [2,3], k = 7, edges = [[0,1]]
Output: 9
Explanation: Alice can achieve the maximum sum of 9 using a single operation:
- Choose the edge [0,1]. nums[0] becomes: 2 XOR 7 = 5 and nums[1] become: 3 XOR 7 = 4, and the array nums becomes: [2,3] -> [5,4].
The total sum of values is 5 + 4 = 9.
It can be shown that 9 is the maximum achievable sum of values.

Example 3:

Input: nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
Output: 42
Explanation: The maximum achievable sum is 42 which can be achieved by Alice performing no operations.

 

Constraints:

    2 <= n == nums.length <= 2 * 10^4
    1 <= k <= 10^9
    0 <= nums[i] <= 10^9
    edges.length == n - 1
    edges[i].length == 2
    0 <= edges[i][0], edges[i][1] <= n - 1
    The input is generated such that edges represent a valid tree.

Hints:
- Select any node as the root.
- Let dp[x][c] be the maximum sum we can get for the subtree rooted at node x, where c is a boolean representing whether the edge between node x and its parent (if any) is selected or not.
- dp[x][c] = max(sum(dp[y][cy]) + v(nums[x], sum(cy) + c)) where cy is 0 or 1. When sum(cy) + c is odd, v(nums[x], sum(cy) + c) = nums[x] XOR k. When sum(cy) + c is even, v(nums[x], sum(cy) + c) = nums[x].
- There's also an easier solution - does the parity of the number of elements where nums[i] XOR k > nums[i] help?    
"""

from typing import List


class Solution1:
    """
    leetcode solution 1: Top-Down Dynamic Programming - Memoization
    Runtime: 1109 ms, faster than 21.59% of Python3 online submissions for Find the Maximum Sum of Node Values.
    Memory Usage: 29.7 MB, less than 17.61% of Python3 online submissions for Find the Maximum Sum of Node Values.
    """

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        memo = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)

    def maxSumOfNodes(self, index, isEven, nums, k, memo):
        if index == len(nums):
            # If the operation is performed on an odd number of elements return INT_MIN
            return 0 if isEven == 1 else -float("inf")
        if memo[index][isEven] != -1:
            return memo[index][isEven]

        # No operation performed on the element
        noXorDone = nums[index] + \
            self.maxSumOfNodes(index + 1, isEven, nums, k, memo)
        # XOR operation is performed on the element
        xorDone = (nums[index] ^ k) + self.maxSumOfNodes(
            index + 1, isEven ^ 1, nums, k, memo
        )

        # Memoize and return the result
        memo[index][isEven] = max(xorDone, noXorDone)
        return memo[index][isEven]


class Solution2:
    """
    leetcode solution 2: Bottom-up Dynamic Programming (Tabulation)
    Runtime: 1045 ms, faster than 28.98% of Python3 online submissions for Find the Maximum Sum of Node Values.
    Memory Usage: 28 MB, less than 67.05% of Python3 online submissions for Find the Maximum Sum of Node Values.
    """

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = 0
        dp[n][0] = -float('inf')

        for index in range(n - 1, -1, -1):
            for isEven in range(2):
                # Case 1: we perform an operation on this element.
                performOperation = dp[index +
                                      1][isEven ^ 1] + (nums[index] ^ k)
                # Case 2: we don't perform operation on this element.
                dontPerformOperation = dp[index + 1][isEven] + nums[index]

                dp[index][isEven] = max(performOperation, dontPerformOperation)

        return dp[0][1]


class Solution3:
    """
    leetcode solution 3: Greedy (Sorting based approach)
    Runtime: 950 ms, faster than 81.82% of Python3 online submissions for Find the Maximum Sum of Node Values.
    Memory Usage: 28.2 MB, less than 50.57% of Python3 online submissions for Find the Maximum Sum of Node Values.
    """

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        netChange = [(nums[i] ^ k) - nums[i] for i in range(n)]
        nodeSum = sum(nums)

        netChange.sort(reverse=True)

        for i in range(0, n, 2):
            # If netChange contains odd number of elements break the loop
            if i + 1 == n:
                break
            pairSum = netChange[i] + netChange[i + 1]
            # Include in nodeSum if pairSum is positive
            if pairSum > 0:
                nodeSum += pairSum

        return nodeSum


class Solution4:
    """
    leetcode solution 4: Greedy (Finding local maxima and minima)
Runtime: 928 ms, faster than 97.73% of Python3 online submissions for Find the Maximum Sum of Node Values.
    Memory Usage: 28.5 MB, less than 19.89% of Python3 online submissions for Find the Maximum Sum of Node Values.    
    """

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sumVal = 0
        count = 0
        positiveMinimum = 1 << 30
        negativeMaximum = -1 * (1 << 30)

        for nodeValue in nums:
            operatedNodeValue = nodeValue ^ k
            sumVal += nodeValue
            netChange = operatedNodeValue - nodeValue
            if netChange > 0:
                positiveMinimum = min(positiveMinimum, netChange)
                sumVal += netChange
                count += 1
            else:
                negativeMaximum = max(negativeMaximum, netChange)

        # If the number of positive netChange values is even, return the sum.
        if count % 2 == 0:
            return sumVal

        # Otherwise return the maximum of both discussed cases.
        return max(sumVal - positiveMinimum, sumVal + negativeMaximum)
