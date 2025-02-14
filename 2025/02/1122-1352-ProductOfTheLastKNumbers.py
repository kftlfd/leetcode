"""
Leetcode
2025-02-14
1352. Product of the Last K Numbers
Medium
Topics
Companies
Hint

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

    ProductOfNumbers() Initializes the object with an empty stream.
    void add(int num) Appends the integer num to the stream.
    int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.

The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 

 

Constraints:

    0 <= num <= 100
    1 <= k <= 4 * 10^4
    At most 4 * 10^4 calls will be made to add and getProduct.
    The product of the stream at any point in time will fit in a 32-bit integer.

 
Follow-up: Can you implement both GetProduct and Add to work in O(1) time complexity instead of O(k) time complexity?

Hint 1
Keep all prefix products of numbers in an array, then calculate the product of last K elements in O(1) complexity.
Hint 2
When a zero number is added, clean the array of prefix products.
"""

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


class ProductOfNumbers00:
    """
    Time Limit Exceeded
    """

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        out = 1
        for num in self.nums[-k:]:
            out *= num
        return out


class ProductOfNumbers01:
    """
    Runtime 105ms Beats 12.63%
    Memory 143.58MB Beats 5.63%
    """

    def __init__(self):
        self.total_product = 1
        self.last_zero_idx = -1
        self.nums = []

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero_idx = len(self.nums)
        else:
            self.total_product *= num
        self.nums.append(self.total_product)

    def getProduct(self, k: int) -> int:
        start_i = len(self.nums) - k
        if start_i <= self.last_zero_idx:
            return 0
        if start_i == 0:
            return self.total_product
        return self.total_product // self.nums[start_i - 1]


class ProductOfNumbers1:
    """
    leetcode solution: Prefix Product
    Runtime 31ms Beats 76.10%
    Memory 31.78MB Beats 37.60%
    """

    def __init__(self):
        # Initialize the product list with 1 to handle multiplication logic
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            # If num is 0, reset the cumulative products since multiplication
            # with 0 invalidates previous products
            self.prefix_product = [1]
            self.size = 0
        else:
            # Append the cumulative product of the current number with the last
            # product
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        # Check if the requested product length exceeds the size of the valid
        # product list
        if k > self.size:
            return 0
        # Compute the product of the last k elements using division
        return (
            self.prefix_product[self.size] // self.prefix_product[self.size - k]
        )
