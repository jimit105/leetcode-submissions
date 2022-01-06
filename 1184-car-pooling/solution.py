# Approach 1 - Time Stamp

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []
        
        for trip in trips:
            timestamps.append([trip[1], trip[0]]) # from, num_passengers
            timestamps.append([trip[2], -trip[0]]) # to, -num_passengers | negative num_passengers since the passengers are dropped
                    
        timestamps.sort()
        
        capacity_used = 0
        for time, passenger_change in timestamps:
            capacity_used += passenger_change
            
            if capacity_used > capacity:
                return False
            
        return True
        
