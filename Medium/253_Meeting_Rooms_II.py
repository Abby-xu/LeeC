class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort(key=lambda x: x[0])
        for x, y in intervals:
            if not heap or heap[0] > x:
                # rooms are still in use
                # The room is still in use, add (push a new end time to min heap) a new room
                heapq.heappush(heap, y)
            else: # free room available , replace with current meeting 
                # If the new start time is greater than or equal to the exist end time, means the room has been released, replace the previous time with the new ending time
                heapq.heappushpop(heap,y)

        return len(heap)
