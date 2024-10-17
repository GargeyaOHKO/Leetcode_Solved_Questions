class Solution:
    def maximumSwap(self, num: int) -> int:
        fl=[]
        l=list(str(num))
        prefix=[]
        m=0
        index=0
        for i in range(len(l)-1,-1,-1):
            if m<int(l[i]):
                m=int(l[i])
                index=i
            prefix.append([str(m),index])
        prefix.reverse()
        #print(prefix)
        for i in range(len(l)):
            l[i],l[prefix[i][1]]=l[prefix[i][1]],l[i]
            fl.append(int("".join(l)))
            l[i],l[prefix[i][1]]=l[prefix[i][1]],l[i]
        return max(fl)