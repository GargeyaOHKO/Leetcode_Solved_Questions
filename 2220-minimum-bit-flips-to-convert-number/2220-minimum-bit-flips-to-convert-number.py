class Solution(object):
    def minBitFlips(self, start, goal):
        c=0
        while max(start,goal)>0:
            bit1=start&1
            bit2=goal&1
            if bit1^bit2==1:
                c+=1
            start=start>>1
            goal=goal>>1    
        return c
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        