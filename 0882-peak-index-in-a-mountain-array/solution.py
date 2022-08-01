# Approach 2: Binary Search
    
# Time: O(log N)
# Space: O(1)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
                
        return low
        
