# Approach 1: Sorting and Median

# m = no. of rows, n = no. of cols
# Time: O(m * n * log mn)
# Space: O(m * n)


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_array = []
        result = 0

        for row in grid:
            for num in row:
                nums_array.append(num)

        nums_array.sort()

        length = len(nums_array)
        final_common_number = nums_array[length // 2]

        for number in nums_array:
            if number % x != final_common_number % x:
                return -1

            result += abs(final_common_number - number) // x

        return result
        
