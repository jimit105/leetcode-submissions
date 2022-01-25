# Approach 1 - One Pass

# Time: O(N)
# Space: O(1)

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        
        # increasing i.e. walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
            
        # peak can't be first or last element
        if i == 0 or i == n- 1:
            return False
    
        # decreasing i.e. walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
            
        return i == n - 1
        
