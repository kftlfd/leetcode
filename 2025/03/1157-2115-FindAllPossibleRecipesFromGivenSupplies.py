"""
Leetcode
2025-03-21
2115. Find All Possible Recipes from Given Supplies
Medium

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

 

Constraints:

    n == recipes.length == ingredients.length
    1 <= n <= 100
    1 <= ingredients[i].length, supplies.length <= 100
    1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
    recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
    All the values of recipes and supplies combined are unique.
    Each ingredients[i] does not contain any duplicate values.


Hint 1
Can we use a data structure to quickly query whether we have a certain ingredient?
Hint 2
Once we verify that we can make a recipe, we can add it to our ingredient data structure. We can then check if we can make more recipes as a result of this.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Runtime 460ms Beats 12.48%
    Memory 19.60MB Beats 94.65%
    """

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        recipes = dict(zip(recipes, ingredients))
        ans = []

        changes = True
        while changes:
            changes = False
            for rec in list(recipes.keys()):
                can_make = True
                for ingr in recipes[rec]:
                    if ingr not in supplies:
                        can_make = False
                        break
                if can_make:
                    ans.append(rec)
                    supplies.add(rec)
                    del recipes[rec]
                    changes = True

        return ans


class Solution1:
    """
    leetcode solution 1: Breadth-First Search (BFS)
    Runtime 695ms Beats 8.59%
    Memory 19.55MB Beats 94.65%
    """

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Track available ingredients and recipes
        available = set(supplies)

        # Queue to process recipe indices
        recipe_queue = deque(range(len(recipes)))
        created_recipes = []
        last_size = -1  # Tracks last known available count

        # Continue while we keep finding new recipes
        while len(available) > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)

            # Process all recipes in current queue
            while queue_size > 0:
                queue_size -= 1
                recipe_idx = recipe_queue.popleft()
                if all(
                    ingredient in available
                    for ingredient in ingredients[recipe_idx]
                ):
                    # Recipe can be created - add to available items
                    available.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)

        return created_recipes


class Solution2:
    """
    leetcode solution 2: Depth-First Search (DFS)
    Runtime 108ms Beats 33.71%
    Memory 27.56MBB eats 6.24%
    """

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Initialize tracking dictionaries using comprehensions
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            # Already processed and can be made
            if can_make.get(recipe, False):
                return True

            # Not a valid recipe or cycle detected
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)

            # Check if all ingredients can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]


class Solution3:
    """
    leetcode solution 3: Topological Sort (Kahn's Algorithm)
    Runtime 24ms Beats 95.87%
    Memory 19.71MB Beats 58.27%
    """

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Store available supplies
        available_supplies = set(supplies)
        # Map recipe to its index
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        # Map ingredient to recipes that need it
        dependency_graph = defaultdict(list)
        # Count of non-supply ingredients needed for each recipe
        in_degree = [0] * len(recipes)

        # Build dependency graph
        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    in_degree[recipe_idx] += 1

        # Start with recipes that only need supplies
        queue = deque(idx for idx, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        # Process recipes in topological order
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            # Skip if no recipes depend on this one
            for dependent_recipe in dependency_graph[recipe]:
                in_degree[recipe_to_index[dependent_recipe]] -= 1
                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    queue.append(recipe_to_index[dependent_recipe])

        return created_recipes
