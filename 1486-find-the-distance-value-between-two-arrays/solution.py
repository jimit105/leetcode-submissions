# Approach: Binary Search

# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/discuss/1170388/Python-code-using-Binary-Search

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        for x in arr1:
            left, right = 0, len(arr2) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if abs(arr2[mid] - x) <= d:
                    break
                    
                elif arr2[mid] > x:
                    right = mid - 1
                    
                else:
                    left = mid + 1
                    
            else:
                count += 1
                
        return count
                
        
