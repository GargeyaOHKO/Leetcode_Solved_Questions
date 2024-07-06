class Solution(object):
    def passThePillow(self, n, time):
        time+=1
        while time>0:
            for i in range(1,n+1):
                time-=1
                if time==0:
                    return i
            for i in range(n-1,1,-1):
                time-=1
                if time==0:
                    return i
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        