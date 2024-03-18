class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        l=[1]*(n)
        l[0]=l[1]=0
        for i in range(2,int(n**0.5)+1):
            if l[i]==1:
                for j in range(i*i,n,i):
                    l[j]=0            
        return sum(l)
        