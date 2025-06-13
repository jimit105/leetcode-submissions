class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def countValidPairs(threshold):
            idx, count = 0, 0
            while idx < n - 1:
                # If a valid pair is found, skip both numbers
                if nums[idx + 1] - nums[idx] <= threshold:
                    count += 1
                    idx += 1
                idx += 1

            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1

        return left

