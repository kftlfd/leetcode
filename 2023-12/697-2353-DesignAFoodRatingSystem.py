"""
Leetcode
2353. Design a Food Rating System
Medium
2023-12-17

Design a food rating system that can do the following:

    Modify the rating of a food item listed in the system.
    Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:

    FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
        foods[i] is the name of the ith food,
        cuisines[i] is the type of cuisine of the ith food, and
        ratings[i] is the initial rating of the ith food.
    void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
    String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:

Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

 

Constraints:

    1 <= n <= 2 * 104
    n == foods.length == cuisines.length == ratings.length
    1 <= foods[i].length, cuisines[i].length <= 10
    foods[i], cuisines[i] consist of lowercase English letters.
    1 <= ratings[i] <= 108
    All the strings in foods are distinct.
    food will be the name of a food item in the system across all calls to changeRating.
    cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
    At most 2 * 104 calls in total will be made to changeRating and highestRated.

Hints:
- The key to solving this problem is to properly store the data using the right data structures.
- Firstly, a hash table is needed to efficiently map each food item to its cuisine and current rating.
- In addition, another hash table is needed to map cuisines to foods within each cuisine stored in an ordered set according to their ratings.
"""

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

from sortedcontainers import SortedSet
from collections import defaultdict
import heapq
from typing import List


class FoodRatings:
    """
    leetcode solution 1: Hash Maps and Priority Queue
    Runtime: 826 ms, faster than 42.01% of Python3 online submissions for Design a Food Rating System.
    Memory Usage: 49.8 MB, less than 24.85% of Python3 online submissions for Design a Food Rating System.
    """

    class Food:
        def __init__(self, food_rating, food_name):
            # Store the food's rating.
            self.food_rating = food_rating
            # Store the food's name.
            self.food_name = food_name

        def __lt__(self, other):
            # Overload the less than operator for comparison.
            # If food ratings are the same, sort based on their name
            # (lexicographically smaller name food will be on top).
            if self.food_rating == other.food_rating:
                return self.food_name < other.food_name
            # Sort based on food rating (bigger rating food will be on top).
            return self.food_rating > other.food_rating

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map food with its rating.
        self.food_rating_map = {}
        # Map food with the cuisine it belongs to.
        self.food_cuisine_map = {}
        # Store all food of a cuisine in a priority queue (to sort them on ratings/name).
        # Priority queue element -> Food: (food_rating, food_name)
        self.cuisine_food_map = defaultdict(list)

        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in
            # 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # Insert the '(rating, name)' element into the current cuisine's priority queue.
            heapq.heappush(self.cuisine_food_map[cuisines[i]], self.Food(
                ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        # Update food's rating in 'food_rating' map.
        self.food_rating_map[food] = newRating
        # Insert the '(new rating, name)' element in the respective cuisine's priority queue.
        cuisineName = self.food_cuisine_map[food]
        heapq.heappush(
            self.cuisine_food_map[cuisineName], self.Food(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the highest rated 'food' of 'cuisine'.
        highest_rated = self.cuisine_food_map[cuisine][0]

        # If the latest rating of 'food' doesn't match with the 'rating'
        # on which it was sorted in the priority queue,
        # then we discard this element from the priority queue.
        while self.food_rating_map[highest_rated.food_name] != highest_rated.food_rating:
            heapq.heappop(self.cuisine_food_map[cuisine])
            highest_rated = self.cuisine_food_map[cuisine][0]

        # Return the name of the highest-rated 'food' of 'cuisine'.
        return highest_rated.food_name


class FoodRatings2:
    """
    leetcode solution 2: Hash Maps and Sorted Set
    Runtime: 1001 ms, faster than 21.90% of Python3 online submissions for Design a Food Rating System.
    Memory Usage: 51.6 MB, less than 18.34% of Python3 online submissions for Design a Food Rating System.
    """

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map food with its rating.
        self.food_rating_map = {}
        # Map food with cuisine it belongs to.
        self.food_cuisine_map = {}

        # Store all food of a cuisine in a set (to sort them on ratings/name)
        # Set element -> Tuple: (-1 * food_rating, food_name)
        self.cuisine_food_map = defaultdict(SortedSet)

        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in
            # 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # Insert the '(-1 * rating, name)' element in the current cuisine's set.
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        # Fetch cuisine name for food.
        cuisine_name = self.food_cuisine_map[food]

        # Find and delete the element from the respective cuisine's set.
        old_element = (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine_name].remove(old_element)

        # Update food's rating in 'food_rating' map.
        self.food_rating_map[food] = newRating
        # Insert the '(-1 * new rating, name)' element in the respective cuisine's set.
        self.cuisine_food_map[cuisine_name].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        # Return name of the highest-rated 'food' of 'cuisine'.
        return highest_rated[1]
