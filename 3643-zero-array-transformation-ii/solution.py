# Approach 2: Line Sweep

# N = len(nums), M = len(queries)
# Time: O(N + M)
# Space: O(N)

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        k = 0
        diff_array = [0] * (n + 1)

        for index in range(n):
            # Iterate through queries while current index of nums cannot equal zero
            while total_sum + diff_array[index] < nums[index]:
                k += 1

                # Zero array isn't formed after all queries are processed
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Process start and end of range
                if right >= index:
                    diff_array[max(left, index)] += val
                    diff_array[right + 1] -= val

            # Update prefix sum at current index
            total_sum += diff_array[index]

        return k

        
