class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        l=[]
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])<=maxDiff:
                l.append(True)
            else:
                l.append(False)

        d=defaultdict(int)
        c=1
        for i in range(len(nums)):
            d[i]=c
            if i<len(nums)-1 and l[i]==False:
                c+=1

        res=[]
        for i in queries:
            if d[i[0]]==d[i[1]]:
                res.append(True)
            else:
                res.append(False)
        return res