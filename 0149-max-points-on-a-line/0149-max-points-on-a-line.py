class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<3:
            return len(points)
        maxi=float('-inf')
        for i in range(len(points)):
            d=defaultdict(int)
            for j in range(i+1,len(points)):
                A=points[i]
                B=points[j]
                if B[0]-A[0]==0:
                    s=float('inf')
                else:
                    s=(B[1]-A[1])/(B[0]-A[0])
                d[s]+=1
                maxi=max(maxi,d[s])
        return maxi+1
