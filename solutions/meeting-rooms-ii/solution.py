class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[0])
        print(intervals)

        heap = []

        for start, end in intervals:
            if heap and start>=heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)

































        # for i in range(1,len(intervals)):
        #     start, end = interval[i][0], interval[i][1]
        #     prev_start, prev_end = intervals[i-1][1]
        #     if start >= prev_start and start < prev_end:
        #         rooms += 1

        # min_start = min([i[0] for i in intervals])
        # max_end = max([i[1] for i in intervals])
        
        # # ind = 0
        # # rooms = 0
        # # i = min_start
        # # while i < max_end:
        # #     while ind <len(intervals) and i >= intervals[ind][0] and i < intervals[ind][1]:
        # #         rooms += 1
        # #         ind += 1
        # #     #rooms -= 1
        # #     i += 1
        # # return rooms

        # def current_rooms(i,intervals): # return how many intervals is point i inside
        #     count = 0
        #     for interval in intervals:
        #         if i >= interval[0] and i < interval[1]:
        #             count += 1
        #     return count

        # at_max_rooms = 1
        # for i in range(min_start,max_end+1):
        #     at_max_rooms = max(at_max_rooms, current_rooms(i,intervals))
        # return at_max_rooms
            







        #     curr = i
        #     while curr <len(intervals) and intervals[curr][0]< intervals[curr-1][1]:
        #         rooms += 1
        #         curr += 1
        # return rooms
        