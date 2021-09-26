class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[curr] = i
