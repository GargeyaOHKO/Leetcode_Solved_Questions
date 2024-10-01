class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l=[]
        s=""
        for i in nums:
            l.append(list(str(i)))
        l.sort()
        l.reverse()
        print(l)
        i=0
        while i<(len(l)-1):
            if int("".join(l[i])+"".join(l[i+1]))<int("".join(l[i+1])+"".join(l[i])):
                l[i],l[i+1]=l[i+1],l[i]
                if i>0:
                    i-=1
            else:
                i+=1
        #print(l)
        s=""
        for i in l:
            s+="".join(i)
        return str(int(s))