class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for i in tasks:
            d[i]=d.get(i,0)+1
        l=[]
        for i in d:
            l.append([d[i],i])
        l.sort(reverse=True)
        c=0
        flag=True
        while flag:
            #print(l)
            flag=False
            gap=n+1
            rem=0
            for i in l:
                if i[0]>0:
                    i[0]-=1
                    rem+=i[0]
                    c+=1
                    gap-=1
                    flag=True
                if gap==0:
                    break
            if gap>0 and flag and rem>0:
                c+=gap
            l.sort(reverse=True)
            #print(c)
        return c
