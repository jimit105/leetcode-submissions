# Approach 2 - Using Array Sort

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        
        capacity = truckSize
        max_units = 0
        
        for num_box, units in boxTypes:
            boxes_to_load = min(capacity, num_box)
            if boxes_to_load <= 0:
                break
            max_units += units * boxes_to_load
            capacity -= boxes_to_load
            
        return max_units
        
