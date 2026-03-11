class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        mdiff=float('-inf')
        sindex=-1
        l=[]
        for i in range(len(gas)):
            l.append(gas[i]-cost[i])
        for i in range(len(gas)):
            l.append(l[i])
        s=0
        c=0
        index=-1
        for i in range(len(l)):
            s+=l[i]
            if s<0:
                index=-1
                s=0
                c=0
            else:
                if index==-1:
                    index=i
                c+=1
                if c==len(gas):
                    return index
        return -1