class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        n=numBottles
        e=numExchange
        s=numBottles
        empty=s
        ret=0
        while empty>=e:
            #print(ret,s,empty)
            ret=empty//e
            s+=ret
            #print(ret*e)
            empty=empty-(ret*e)+ret
            #print(ret,s,empty)
        return s
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        