# Approach 1: Breadth-First Search (BFS)

# n = len(reciples), m = total ingredients, s = len(supplies)
# Time: O(n * m + s)
# Space: O(n + s)

from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)

        # Recipe indices
        recipe_queue = deque(range(len(recipes)))
        created_recipes = []
        last_size = -1

        while len(available) > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)

            while queue_size > 0:
                queue_size -= 1
                recipe_idx = recipe_queue.popleft()

                if all(ingredient in available for ingredient in ingredients[recipe_idx]):
                    available.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)

        return created_recipes
        
