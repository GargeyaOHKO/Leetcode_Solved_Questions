class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        st=[]
        s=0
        for i in range(30,-1,-1):
            if (2**i)+s>start:
                st.append(0)
            else:
                s+=2**i
                st.append(1)
        end=[]
        s=0
        for i in range(30,-1,-1):
            if (2**i)+s>goal:
                end.append(0)
            else:
                s+=2**i
                end.append(1)
        #print(st)
        #print(end)
        c=0
        for i in range(len(st)):
            if st[i]!=end[i]:
                c+=1
        return c
        