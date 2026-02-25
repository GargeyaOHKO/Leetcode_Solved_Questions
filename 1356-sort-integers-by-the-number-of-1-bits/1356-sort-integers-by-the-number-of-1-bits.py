class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res=[[] for _ in range(20)]
        for i in arr:
            b=bin(i)[2:]
            b+='0'
            d=Counter(b)
            #print(d)
            res[d['1']].append(i)

        ans=[]
        for i in res:
            i.sort()
            for j in i:
                ans.append(j)
        return ans




