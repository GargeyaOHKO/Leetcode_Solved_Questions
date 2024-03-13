class Solution:
    def pivotInteger(self, n: int) -> int:
        l1=[]
        l2=[]
        c=0
        if n==1:
            return 1
        for i in range(1,n+1):
            c+=i
            l1.append(c)
        for i in range(1,n):
            l2.append(c) 
            c-=i
        print(l1)
        print(l2)    
        for i in range(1,len(l1)-1):
            if l1[i]==l2[i]:
                return i+1
        return -1        

        