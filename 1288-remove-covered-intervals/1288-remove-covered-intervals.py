class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        newintervals=[]
        for i in intervals:
            newintervals.append([i[0],0-(i[1]-i[0]),i[1]])
        newintervals.sort()
        intervals=[]
        for i in newintervals:
            intervals.append([i[0],i[2]])
        i=0
        l=[]
        while i<len(intervals):
            #print(i)
            start,end=intervals[i][0],intervals[i][1]
            while i+1<len(intervals) and start<=intervals[i+1][0] and end>=intervals[i+1][1]:
                i+=1
                continue
            l.append([start,end])
            i+=1
        #print(l)
        return len(l)

