class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        res=[]
        i,j=0,0
        while i<len(series1) or j<len(series2):
            if i>=len(series1) and j<len(series2):
                res.append([series2[j][0],series2[j][1]])
                j+=1
                continue
            if j>=len(series2) and i<len(series1):
                res.append([series1[i][0],series1[i][1]])
                i+=1
                continue
            if series1[i][0]==series2[j][0]:
                res.append([series1[i][0],series1[i][1]+series2[j][1]])
                i+=1
                j+=1
            elif series1[i][0]<series2[j][0]:
                res.append([series1[i][0],series1[i][1]+series2[j][1]])
                i+=1
            elif series1[i][0]>series2[j][0]:
                res.append([series2[j][0],series1[i][1]+series2[j][1]])
                j+=1
        return res
