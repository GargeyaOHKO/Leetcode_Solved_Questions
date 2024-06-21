class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        s=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                s+=customers[i]
        
        l,r=0,0
        maxs=0
        while r<len(customers):
            #print(l,r)
            s1=s
            if r-l<minutes:
                r+=1
            else:
                r+=1
                l+=1
            #print(l,r)
            for i in range(l,r):
                if grumpy[i]==1:
                    s1+=customers[i]
            maxs=max(maxs,s1)
        return maxs
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        