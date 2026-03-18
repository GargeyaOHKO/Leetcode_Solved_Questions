class Solution:
    def magicalString(self, n: int) -> int:
        if n==1:
            return 1
        if n==2 or n==3:
            return 1
        c=1
        l,r=2,0
        res=[1,2,2]
        total=3
        while total<n:
            #print(l,res)
            if l%2==0:
                #print(l,res)
                for i in range(res[l]):
                    if total>=n:
                        break
                    res.append(1)
                    c+=1
                    total+=1
                l+=1
            else:
                for i in range(res[l]):
                    if total>=n:
                        break
                    res.append(2)
                    total+=1
                l+=1
            r+=1 
        #print(res)
        return c