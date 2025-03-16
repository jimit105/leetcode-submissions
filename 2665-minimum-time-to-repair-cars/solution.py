# Approach 2: Space Optimized Binary Search

# n = len(ranks), m = len(cars)
# Time: O(n * log(m * max_rank))
# Space: O(1)

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, cars * cars * max(ranks)

        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)

            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid

        return low
        
