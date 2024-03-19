class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        c=0
        high=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=high:
                high=min(points[i][1],high)
                continue
            else:
                high=points[i][1]
                c+=1
        return c+1       
        """
        :type points: List[List[int]]
        :rtype: int
        """
        