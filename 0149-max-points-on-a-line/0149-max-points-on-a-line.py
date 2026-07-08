class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<3:
            return len(points)
        maxi=float('-inf')
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                A=points[i]
                B=points[j]
                c=0
                for k in range(len(points)):
                    C=points[k]
                    if ((C[1]-B[1])*(B[0]-A[0]))-((B[1]-A[1])*(C[0]-B[0]))==0:
                        c+=1
                maxi=max(maxi,c)
        return maxi
