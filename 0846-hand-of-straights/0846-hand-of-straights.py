class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        d={}
        for i in hand:
            d[i]=d.get(i,0)+1
        d={k:d[k] for k in sorted(d)}

        c=0
        while c!=len(hand):
            k=groupSize
            l=[]
            for i in d:
                if k==0:
                    break
                if d[i]!=0:
                    print(i)    
                    if l==[]:
                        l.append(i)
                    elif l[-1]!=i-1:
                        return False
                    else:
                        l.append(i)    
                    d[i]-=1
                    k-=1            
                    c+=1
        return True
         

        