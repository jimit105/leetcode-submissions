import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        free_rooms = []
        
        intervals.sort(key=lambda x: x[0])
        
        # Allocate room for the first meeting
        heapq.heappush(free_rooms, intervals[0][1])
        
        for meeting in intervals[1:]:
            
            # If the earliest end time in the heap is before the start of the current meeting, then allocate the same room i.e. update the end time in the heap
            if free_rooms[0] <= meeting[0]:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, meeting[1])
            
        return len(free_rooms)
        
