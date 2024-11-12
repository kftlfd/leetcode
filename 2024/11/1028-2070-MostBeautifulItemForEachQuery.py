"""
Leetcode
2024-11-12
2070. Most Beautiful Item for Each Query
Medium

You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

Example 1:

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.

Example 2:

Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.  

Example 3:

Input: items = [[10,1000]], queries = [5]
Output: [0]
Explanation:
No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0.

 

Constraints:

    1 <= items.length, queries.length <= 10^5
    items[i].length == 2
    1 <= pricei, beautyi, queries[j] <= 10^9
"""

from functools import cache
from typing import List


class Solution:
    """
    Runtime: 203 ms, faster than 60.98% of Python3 online submissions for Most Beautiful Item for Each Query.
    Memory Usage: 66.2 MB, less than 61.83% of Python3 online submissions for Most Beautiful Item for Each Query.
    """

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        price_beauty = []
        max_beauty = 0
        prev_price = 0

        for price, beauty in sorted(items):
            max_beauty = max(max_beauty, beauty)
            if price != prev_price:
                price_beauty.append([price, max_beauty])
                prev_price = price
            else:
                price_beauty[-1][1] = max_beauty

        @cache
        def find_max_beauty(price: int) -> int:
            left = 0
            right = len(price_beauty)

            while left < right:
                mid = (left + right) // 2
                val = price_beauty[mid]
                if val[0] <= price:
                    left = mid + 1
                else:
                    right = mid

            if right <= 0:
                return 0

            return price_beauty[right - 1][1]

        return [find_max_beauty(price) for price in queries]


class Solution2:
    """
    leetcode solution 2: Sorting Items + Sorting Queries
    Runtime: 147 ms, faster than 69.51% of Python3 online submissions for Most Beautiful Item for Each Query.
    Memory Usage: 64.8 MB, less than 75.27% of Python3 online submissions for Most Beautiful Item for Each Query.
    """

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)

        # sort both items and queries in ascending order
        items.sort(key=lambda x: x[0])

        queries_with_indices = [[queries[i], i] for i in range(len(queries))]

        queries_with_indices.sort(key=lambda x: x[0])

        item_index = 0
        max_beauty = 0

        for i in range(len(queries)):
            query = queries_with_indices[i][0]
            original_index = queries_with_indices[i][1]

            while item_index < len(items) and items[item_index][0] <= query:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1

            ans[original_index] = max_beauty

        return ans
