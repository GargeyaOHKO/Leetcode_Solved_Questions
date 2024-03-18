class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        l=[0]*(n)
        for i in range(2,int(n**0.5)+1):
            if l[i]==0:
                for j in range(i*i,n,i):
                    l[j]=1
        c=0        
        for i in range(2,n):
            if l[i]==0:
                c+=1               
        return c
        