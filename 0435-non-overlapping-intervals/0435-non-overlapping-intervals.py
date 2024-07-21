class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        l=intervals[0][1]
        c=1
        for i in range(1,len(intervals)):
            if l<=intervals[i][0]:
                c+=1
                l=intervals[i][1]
        return len(intervals)-c

        