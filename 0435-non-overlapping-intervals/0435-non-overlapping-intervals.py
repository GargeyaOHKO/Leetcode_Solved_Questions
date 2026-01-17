class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        #print(intervals)
        c=0
        over=intervals[0][1]
        for i in range(1,len(intervals)):
            if over>intervals[i][0]:
                c+=1
            else:
                over=intervals[i][1]
        return c