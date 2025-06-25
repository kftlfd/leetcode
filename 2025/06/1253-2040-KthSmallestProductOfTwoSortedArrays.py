"""
Leetcode
2025-06-25
2040. Kth Smallest Product of Two Sorted Arrays
Hard

Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.

 

Example 1:

Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8.

Example 2:

Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation: The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6th smallest product is 0.

Example 3:

Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation: The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3rd smallest product is -6.

 

Constraints:

    1 <= nums1.length, nums2.length <= 5 * 10^4
    -10^5 <= nums1[i], nums2[j] <= 10^5
    1 <= k <= nums1.length * nums2.length
    nums1 and nums2 are sorted.


Hint 1
Can we split this problem into four cases depending on the sign of the numbers?
Hint 2
Can we binary search the value?
"""

from bisect import bisect_left, bisect_right
from typing import List


class Solution1:
    """
    leetcode solution 1: Binary Search + Binary Search
    Runtime 3801ms Beats 24.38%
    Memory 25.66MB Beats 85.57%
    """

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        According to the problem's constraints, the value range of nums1[i]*nums2[j] is [-1010,1010]. 
        We perform a binary search over this product range to find the k-th smallest product. Let 
        the current binary search value be v. We need to compute the number of products less than or 
        equal to v, denoted as count. If count<k, then v is too small; otherwise, it is too large or 
        just right.

        To calculate the number of products less than or equal to v, we use another binary search. 
        For each element x1 in nums1, we proceed as follows:

            If x1≥0, then nums2[j]*x1 forms a non-decreasing sequence. We use binary search to count 
            how many products are ≤v.

            If x1<0, then nums2[j]*x1 forms a non-increasing sequence. In this case, we use binary 
            search to find how many products are greater than v, denoted as t. Then, the number of 
            products ≤v is n2-t, where n2 is the length of nums2.

        Summing these counts for all elements in nums1 gives the total number of products less 
        than or equal to v.
        """

        n1 = len(nums1)
        left, right = -(10**10), 10**10
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for i in range(n1):
                count += self.f(nums2, nums1[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 > 0:
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            return len(nums2) - bisect_left(nums2, -(-v // x1))
        else:
            return len(nums2) if v >= 0 else 0


class Solution2:
    """
    Approach 2: Binary Search + Divide and Conquer
    Runtime 1977ms Beats 81.59%
    Memory 25.75MB Beats 69.15%
    """

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        Similar to Approach 1, we want to compute the number of products less than or equal to a 
        given value v, but here we use a divide and conquer method. Let the lengths of nums1 and 
        nums2 be n1 and n2, respectively. We divide nums1 into two segments: [0,pos1) for values 
        less than 0, and [pos1,n1) for values greater than or equal to 0. Likewise, we divide 
        nums2 into [0,pos2) for values less than 0, and [pos2,n2) for values greater than or equal 
        to 0. This results in four combinations of subarrays whose element-wise products we need 
        to consider.

        For example, take the product of the interval [0,pos1) from nums1 and the interval [0,pos2) 
        from nums2, and count how many resulting products are less than or equal to v. Repeat this 
        process for the other three combinations.

        Each product combination forms a two-dimensional matrix where each cell is defined as 
        q(i,j)=nums1[i]*nums2[j]. In this matrix, q(i,j) is non-increasing as either i or j increases 
        (since both sequences are sorted). To efficiently count the number of elements in the matrix 
        that are ≤v, we traverse from the upper-right corner of the matrix. We initialize pointers 
        i1=0 and i2=pos2-1, and we stop when either index goes out of bounds:

            If q(i1,i2)>v, then all elements in the current row to the left of (i1,i2) are also 
            greater than v, so we move down to the next row by setting i1=i1+1.

            If q(i1,i2)≤v, then all elements in the current column above (i1,i2) are also ≤v. There 
            are pos1-i1 such elements, so we add that count and move left by setting i2=i2-1.

        We repeat this process and sum all such counts. This gives the total number of products less 
        than or equal to v for the given combination of subarrays.
        """

        n1, n2 = len(nums1), len(nums2)
        pos1, pos2 = 0, 0
        while pos1 < n1 and nums1[pos1] < 0:
            pos1 += 1
        while pos2 < n2 and nums2[pos2] < 0:
            pos2 += 1
        left, right = int(-1e10), int(1e10)
        while left <= right:
            mid = (left + right) // 2
            count = 0
            i1, i2 = 0, pos2 - 1
            while i1 < pos1 and i2 >= 0:
                if nums1[i1] * nums2[i2] > mid:
                    i1 += 1
                else:
                    count += pos1 - i1
                    i2 -= 1
            i1, i2 = pos1, n2 - 1
            while i1 < n1 and i2 >= pos2:
                if nums1[i1] * nums2[i2] > mid:
                    i2 -= 1
                else:
                    count += i2 - pos2 + 1
                    i1 += 1
            i1, i2 = 0, pos2
            while i1 < pos1 and i2 < n2:
                if nums1[i1] * nums2[i2] > mid:
                    i2 += 1
                else:
                    count += n2 - i2
                    i1 += 1
            i1, i2 = pos1, 0
            while i1 < n1 and i2 < pos2:
                if nums1[i1] * nums2[i2] > mid:
                    i1 += 1
                else:
                    count += n1 - i1
                    i2 += 1
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
