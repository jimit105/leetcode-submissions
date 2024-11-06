# Approach 2: Sortable Segments

# Time: O(n)
# Space: O(1)

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        num_of_set_bits = bin(nums[0]).count('1')
        max_of_segment = nums[0]
        min_of_segment = nums[0]

        max_of_prev_segment = float('-inf')

        for i in range(len(nums)):

            # element belongs to same segment
            if bin(nums[i]).count('1') == num_of_set_bits:
                # update min and max of segment
                max_of_segment = max(max_of_segment, nums[i])
                min_of_segment = min(min_of_segment, nums[i])

            # element belongs to new segment   
            else:
                # check if segments are arranged properly
                if min_of_segment < max_of_prev_segment:
                    return False

                # update max of previous segment
                max_of_prev_segment = max_of_segment

                # start new segment with current element
                max_of_segment = nums[i]
                min_of_segment = nums[i]
                num_of_set_bits = bin(nums[i]).count('1')

        # final check for proper segment arrangement
        if min_of_segment < max_of_prev_segment:
            return False

        return True
        
