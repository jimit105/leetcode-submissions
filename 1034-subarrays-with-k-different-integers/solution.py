from collections import OrderedDict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        left_idx = 0 # index of the removed element from subarray
        
        od = OrderedDict() # store last index of each element
        for idx, num in enumerate(nums):
            od[num] = idx
            od.move_to_end(num)
            
            while len(od) > k:
                left_idx = od.popitem(last=False)[1] + 1
                
            if len(od) == k:
                ans += next(iter(od.items()))[1] - left_idx + 1
                
        return ans
