class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]

        if newInterval[0]>intervals[-1][1]:
            return intervals.append(newInterval)

        if newInterval[1]<intervals[0][0]:
            new=[]
            new.append(newInterval)
            for i in intervals:
                new.append(i)
            return new

        new=[]
        flag=False
        i=0
        while i<len(intervals):
            #print(new)
            if flag==False:
                if intervals[i][1]>=newInterval[0] and intervals[i][0]>=newInterval[0]:
                    #print("Case 1")
                    start=newInterval[0]
                    j=i
                    while j<len(intervals):
                        #print(j)
                        if newInterval[1]<intervals[j][0]:
                            end=newInterval[1]
                            flag=True
                            break
                        elif newInterval[1]<intervals[j][1]:
                            end=intervals[j][1]
                            flag=True
                            i=j+1
                            break
                        else:
                            end=newInterval[1]
                        j+=1
                        i=j
                    new.append([start,end])
                elif (intervals[i][1]>=newInterval[0] and intervals[i][0]<newInterval[0]) or newInterval[0]==intervals[i][0]:
                    #print("Case 2")
                    start=intervals[i][0]
                    j=i
                    while j<len(intervals):
                        #print(j)
                        if newInterval[1]<intervals[j][0]:
                            end=newInterval[1]
                            flag=True
                            break
                        elif newInterval[1]<intervals[j][1]:
                            end=intervals[j][1]
                            flag=True
                            i=j+1
                            break
                        else:
                            end=newInterval[1]
                        j+=1
                        i=j
                    new.append([start,end])
                else:
                    new.append(intervals[i])
                    i+=1
            else:
                new.append(intervals[i])
                i+=1
        return new