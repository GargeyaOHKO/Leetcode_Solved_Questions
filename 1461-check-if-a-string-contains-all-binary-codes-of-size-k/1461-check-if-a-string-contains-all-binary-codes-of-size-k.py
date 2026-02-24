class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if s=="":
            return False
        st=0
        for i in range(k):
            st+=2**i
        #print(st)
        res=[0]*(st+1)
        curr=collections.deque()
        l,r=0,0
        #print(l,s[l])
        for i in range(k):
            if i<len(s):
                curr.append(s[l])
                l+=1
        l-=1
        while l<len(s):
            power=k-1
            num=0
            for i in curr:
                num+=(2**power)*int(i)
                power-=1
            res[num]=1
            l+=1
            curr.popleft()
            if l<len(s):
                curr.append(s[l])
        #print(res)
        for i in res:
            if i==0:
                return False
        return True
