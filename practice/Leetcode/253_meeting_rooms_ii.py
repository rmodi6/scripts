# https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return len(heap)
