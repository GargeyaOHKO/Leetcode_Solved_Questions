class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d={}
        l=[]
        df={}
        for i in range(len(mapping)):
            d[i]=mapping[i]
        for i in nums:
            s=""
            for j in str(i):
                s+=str(d[int(j)])
            if int(s) not in df:
                l.append(int(s))
                df[int(s)]=[i]
            else:
                df[int(s)].append(i)
        l.sort()
        res=[]
        for i in l:
            for j in df[i]:
                res.append(j)
        return res
