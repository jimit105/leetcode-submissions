import bisect

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        half = len(nums) // 2
        left = bisect.bisect_left(nums, target)
        
        if left > half:
            return False
        
        right = bisect.bisect_right(nums, target, lo=left+half, hi=min(left+half+1, len(nums)))
        
        return (right - left) > half
        
