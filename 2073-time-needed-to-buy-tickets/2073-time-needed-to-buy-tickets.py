class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        i=0
        c=0
        l=len(tickets)
        while tickets[k]!=0:
            if tickets[i%l]>0:
                c+=1
                tickets[i%l]-=1
            i+=1
        return c       
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        