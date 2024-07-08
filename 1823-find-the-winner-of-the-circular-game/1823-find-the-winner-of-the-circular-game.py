class Solution(object):
    def findTheWinner(self, n, k):
        k-=1
        l=[i for i in range(1,n+1)]
        #print(l)
        cur=0
        while len(l)>1:
            nxt=(cur+k)%len(l)
            if nxt<len(l):
                del l[nxt]
                #print(nxt,len(l))
                cur=nxt%len(l)
                #print(l,cur)
            else:
                del l[nxt%len(l)]
                #print(nxt,len(l))
                cur=nxt%len(l)
                #print(l,cur)
        return l[0]
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        