class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        l=[]
        q=deque()
        q.append("")
        while q:
            for z in range(len(q)):
                temp=q.popleft()
                for i in range(97,100,1):
                    #print(q)
                    curr=temp
                    if len(curr)==0 or curr[-1]!=chr(i):
                        curr+=chr(i)
                        if len(curr)==n:
                            l.append(curr)
                        else:
                            q.append(curr)
        #print(l)
        l.sort()
        if k>len(l):
            return ""
        return l[k-1]
