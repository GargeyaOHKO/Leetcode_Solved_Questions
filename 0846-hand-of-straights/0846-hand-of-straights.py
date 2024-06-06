class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d=Counter(hand)
        d={k:d[k] for k in sorted(d)}
        c=0
        while c!=len(hand):
            tempk=groupSize
            for i in d:
                if tempk==0:
                    break
                if d[i]>0:
                    if ((i+1 not in d) or i+1 in d and d[i+1]<1) and tempk!=1:
                        return False
                    tempk-=1
                    d[i]-=1
                    c+=1
        return True
         

        